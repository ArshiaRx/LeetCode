import os
import shutil
from collections import Counter, defaultdict

# Map file extensions to language names
EXT_TO_LANG = {
    ".py": "Python",
    ".java": "Java",
    ".cpp": "C++",
    ".cc": "C++",
    ".cxx": "C++",
    ".c": "C",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".go": "Go",
    ".rb": "Ruby",
    ".rs": "Rust",
    ".cs": "C#",
    ".kt": "Kotlin",
    ".swift": "Swift",
    ".php": "PHP",
    ".sql": "SQL",
    ".scala": "Scala",
    ".sh": "Shell",
}

DIFFICULTIES = ["Easy", "Medium", "Hard"]

def find_solution_files(base_dir: str):
    """
    Find code files under base_dir, excluding markdown/problem statements and hidden folders.
    """
    code_files = []
    for root, dirs, files in os.walk(base_dir):
        # Skip hidden/system dirs
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("__pycache__", "node_modules", ".git")]

        for f in files:
            if f.startswith("."):
                continue
            # ignore common non-solution artifacts
            if f.lower().endswith((".md", ".txt", ".json")):
                continue
            path = os.path.join(root, f)
            code_files.append(path)
    return code_files

def language_from_filename(path: str) -> str:
    _, ext = os.path.splitext(path.lower())
    return EXT_TO_LANG.get(ext, f"Other ({ext or 'no-ext'})")

def pct(n: int, total: int) -> str:
    if total == 0:
        return "0.0%"
    return f"{(n * 100.0 / total):.1f}%"

def parse_folder_name(folder_name: str):
    """
    Parse folder name to extract difficulty, category (optional), and problem name.
    Supports two formats:
    1. Difficulty_Category_id-slug (if category is included)
    2. Difficulty_id-slug (if category is not included)
    
    Returns: (difficulty, category, problem_name)
    """
    for diff in DIFFICULTIES:
        if folder_name.startswith(f"{diff}_"):
            remaining = folder_name[len(diff) + 1:]  # Remove "Medium_" prefix
            
            # Skip if remaining contains literal template variables (means template var not supported)
            if "${" in remaining or "$tags" in remaining:
                # Treat as no category - template variable wasn't expanded
                return (diff, None, remaining)
            
            # Check if there's a category (format: Category_id-slug)
            # Category would be followed by underscore and then digits
            parts = remaining.split("_", 1)
            if len(parts) == 2 and parts[1] and parts[1][0].isdigit():
                # Has category: Category_id-slug
                category = parts[0]
                problem_name = parts[1]
                return (diff, category, problem_name)
            else:
                # No category: id-slug
                return (diff, None, remaining)
    return (None, None, None)

def organize_by_difficulty(leetcode_root: str):
    """
    Move folders like 'Medium_347-top-k-frequent-elements' or 'Medium_Array_238-product-of-array-except-self'
    into 'Medium/347-top-k-frequent-elements/' or 'Medium/238-product-of-array-except-self/'
    
    Returns a dict mapping (difficulty, problem_name) -> category for use in README generation
    """
    category_map = {}
    
    if not os.path.isdir(leetcode_root):
        return category_map
    
    items_to_move = []
    for item in os.listdir(leetcode_root):
        item_path = os.path.join(leetcode_root, item)
        if not os.path.isdir(item_path):
            continue
        
        difficulty, category, problem_name = parse_folder_name(item)
        if difficulty and problem_name:
            dest_dir = os.path.join(leetcode_root, difficulty)
            dest_path = os.path.join(dest_dir, problem_name)
            items_to_move.append((item_path, dest_path, dest_dir, difficulty, problem_name, category))
            # Store category mapping if available
            if category:
                category_map[(difficulty, problem_name)] = category
    
    # Move items after collecting them (to avoid modifying list while iterating)
    for item_path, dest_path, dest_dir, difficulty, problem_name, category in items_to_move:
        os.makedirs(dest_dir, exist_ok=True)
        if os.path.exists(dest_path):
            # If destination already exists, merge new files from source to dest, then delete source
            try:
                for file in os.listdir(item_path):
                    src_file = os.path.join(item_path, file)
                    dst_file = os.path.join(dest_path, file)
                    if os.path.isfile(src_file) and not os.path.exists(dst_file):
                        shutil.copy2(src_file, dst_file)
                        print(f"Copied {file} from {item_path} to {dest_path}")
                # Remove the source folder after merging
                shutil.rmtree(item_path)
                print(f"Merged and removed {item_path}")
            except Exception as e:
                print(f"Warning: Error merging {item_path} into {dest_path}: {e}")
        else:
            shutil.move(item_path, dest_path)
            print(f"Moved {item_path} -> {dest_path}")
    
    # Cleanup sweep: remove any remaining {Difficulty}_* folders at root
    for item in os.listdir(leetcode_root):
        item_path = os.path.join(leetcode_root, item)
        if not os.path.isdir(item_path):
            continue
        
        # Check if it matches the pattern {Difficulty}_*
        for diff in DIFFICULTIES:
            if item.startswith(f"{diff}_"):
                try:
                    shutil.rmtree(item_path)
                    print(f"Cleaned up leftover folder: {item_path}")
                except Exception as e:
                    print(f"Warning: Could not remove leftover folder {item_path}: {e}")
                break
    
    return category_map

def rename_problem_statements(leetcode_root: str):
    """
    Rename problem statement markdown files in each problem folder to README.md.
    Scans Easy/, Medium/, Hard/ directories and looks for .md files (except README.md)
    in each problem subfolder, then renames them to README.md.
    """
    for diff in DIFFICULTIES:
        diff_dir = os.path.join(leetcode_root, diff)
        if not os.path.isdir(diff_dir):
            continue
        
        # Scan each problem folder
        for item in os.listdir(diff_dir):
            problem_folder = os.path.join(diff_dir, item)
            if not os.path.isdir(problem_folder) or item.startswith("."):
                continue
            
            # Look for markdown files in this problem folder
            md_files = []
            if os.path.isdir(problem_folder):
                for file in os.listdir(problem_folder):
                    file_path = os.path.join(problem_folder, file)
                    if os.path.isfile(file_path) and file.lower().endswith(".md"):
                        # Skip if already README.md
                        if file.lower() != "readme.md":
                            md_files.append(file_path)
            
            # If we found markdown files, rename the first one to README.md
            # (Usually leetcode-export only creates one problem statement file)
            if md_files:
                target_readme = os.path.join(problem_folder, "README.md")
                
                # If README.md already exists, skip or replace based on preference
                # Here we'll replace it with the problem statement
                if os.path.exists(target_readme):
                    # Backup old README.md if it's different
                    try:
                        os.remove(target_readme)
                    except Exception as e:
                        print(f"Warning: Could not remove existing README.md in {problem_folder}: {e}")
                        continue
                
                # Rename the first markdown file to README.md
                try:
                    os.rename(md_files[0], target_readme)
                    print(f"Renamed {md_files[0]} -> {target_readme}")
                    
                    # If there are multiple .md files, remove the others
                    # (shouldn't happen normally, but just in case)
                    for other_md in md_files[1:]:
                        try:
                            os.remove(other_md)
                            print(f"Removed duplicate markdown file: {other_md}")
                        except Exception as e:
                            print(f"Warning: Could not remove {other_md}: {e}")
                except Exception as e:
                    print(f"Warning: Could not rename {md_files[0]} to README.md: {e}")

def group_problems_by_category(problem_folders: list, difficulty: str, category_map: dict):
    """
    Group problem folders by category.
    Returns a dict mapping category -> list of problem folders.
    """
    categories = defaultdict(list)
    
    for problem in problem_folders:
        category = category_map.get((difficulty, problem), None)
        categories[category].append(problem)
    
    return categories

def generate_readme_for_difficulty(diff_dir: str, difficulty: str, files: list, lang_counter: Counter, category_map: dict):
    """
    Generate README.md for a specific difficulty folder.
    """
    total_files = sum(lang_counter.values())
    
    lines = []
    lines.append(f"# {difficulty} Problems\n\n")
    lines.append(f"Total solution files: **{total_files}**\n\n")
    
    # Language breakdown
    if lang_counter:
        lines.append("## Language Distribution\n\n")
        lines.append("| Language | Count | Percent |\n")
        lines.append("|---|---:|---:|\n")
        for lang, count in lang_counter.most_common():
            lines.append(f"| {lang} | {count} | {pct(count, total_files)} |\n")
        lines.append("\n")
    
    # Problem list (grouped by category if available)
    problem_folders = []
    if os.path.isdir(diff_dir):
        for item in os.listdir(diff_dir):
            item_path = os.path.join(diff_dir, item)
            if os.path.isdir(item_path) and not item.startswith("."):
                problem_folders.append(item)
    
    problem_folders.sort()
    
    if problem_folders:
        # Group by category
        problems_by_category = group_problems_by_category(problem_folders, difficulty, category_map)
        
        # Check if we have any categories
        has_categories = any(cat is not None for cat in problems_by_category.keys())
        
        if has_categories:
            lines.append("## Problems by Category\n\n")
            # Sort categories alphabetically, but put None (uncategorized) last
            sorted_categories = sorted(
                [cat for cat in problems_by_category.keys() if cat is not None],
                key=lambda x: x or ""
            )
            if None in problems_by_category:
                sorted_categories.append(None)
            
            for category in sorted_categories:
                problems = sorted(problems_by_category[category])
                if category:
                    lines.append(f"### {category}\n\n")
                else:
                    lines.append("### Uncategorized\n\n")
                
                for problem in problems:
                    lines.append(f"- [{problem}](./{problem})\n")
                lines.append("\n")
        else:
            lines.append("## Problems\n\n")
            for problem in problem_folders:
                lines.append(f"- [{problem}](./{problem})\n")
            lines.append("\n")
    
    readme_path = os.path.join(diff_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"Wrote {readme_path}")

def generate_root_readme(leetcode_root: str, results: dict):
    """
    Generate combined README.md at leetcode root.
    """
    lines = []
    lines.append("# LeetCode Solutions\n\n")
    lines.append("This repository contains my LeetCode solutions, organized by difficulty.\n\n")
    
    # Overall stats
    overall = results.get("Overall", {})
    overall_total = overall.get("total_files", 0)
    lines.append(f"Total solution files: **{overall_total}**\n\n")
    
    # Language distribution
    overall_langs = overall.get("languages", {})
    if overall_langs:
        lines.append("## Overall Language Distribution\n\n")
        lines.append("| Language | Count | Percent |\n")
        lines.append("|---|---:|---:|\n")
        for lang, meta in overall_langs.items():
            lines.append(f"| {lang} | {meta['count']} | {meta['percent']} |\n")
        lines.append("\n")
    
    # Breakdown by difficulty
    lines.append("## By Difficulty\n\n")
    for diff in DIFFICULTIES:
        diff_data = results.get(diff, {})
        total_files = diff_data.get("total_files", 0)
        lines.append(f"- [{diff}](./{diff}/) - {total_files} solutions\n")
    lines.append("\n")
    
    readme_path = os.path.join(leetcode_root, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"Wrote {readme_path}")

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    leetcode_root = os.path.join(repo_root, "leetcode")

    # Organize folders by difficulty first and get category mapping
    category_map = organize_by_difficulty(leetcode_root)
    
    # Rename problem statement files to README.md
    rename_problem_statements(leetcode_root)

    results = {}
    overall_counter = Counter()

    # Process each difficulty
    for diff in DIFFICULTIES:
        diff_dir = os.path.join(leetcode_root, diff)
        if not os.path.isdir(diff_dir):
            results[diff] = {"total_files": 0, "languages": {}}
            continue

        files = find_solution_files(diff_dir)
        counter = Counter(language_from_filename(p) for p in files)

        total = sum(counter.values())
        overall_counter.update(counter)

        results[diff] = {
            "total_files": total,
            "languages": {lang: {"count": c, "percent": pct(c, total)} for lang, c in counter.most_common()}
        }
        
        # Generate README for this difficulty
        generate_readme_for_difficulty(diff_dir, diff, files, counter, category_map)

    # Overall stats
    overall_total = sum(overall_counter.values())
    results["Overall"] = {
        "total_files": overall_total,
        "languages": {lang: {"count": c, "percent": pct(c, overall_total)} for lang, c in overall_counter.most_common()}
    }
    
    # Generate root README
    os.makedirs(leetcode_root, exist_ok=True)
    generate_root_readme(leetcode_root, results)

if __name__ == "__main__":
    main()
