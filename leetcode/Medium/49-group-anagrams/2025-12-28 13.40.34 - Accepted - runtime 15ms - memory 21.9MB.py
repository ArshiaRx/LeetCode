class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
           
        # mapping charCount to list of Anagorams
        result = defaultdict(list)

        # We know the input is all lower case from a-z which is 26 char
        # Per each one we need to count how many of each letter they got 
        # Ex: 
        #   eat -- counting it would be 1-e, 1-a, 1,t
        #   If next index contains the same we list them separately

        # Hashmap key: 

        for s in strs:
            count = [0] * 26  # a .. z

            for c in s:

                # ACSII value of each
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)
        
        return list(result.values())   # O(m * n)  # list of list