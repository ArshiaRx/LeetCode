class Solution {
    public boolean isValid(String s) {

        //Stack
        //Empty stack to keep track of items, could be numbers or characters
        Stack<Character> stack = new Stack<Character>();

        for (char c : s.toCharArray()){
            if (c == ')' && !stack.isEmpty() && stack.peek() == '('){
                stack.pop();
            }
            else if (c == '}' && !stack.isEmpty() && stack.peek() == '{'){
                stack.pop();
            }
            else if (c == ']' && !stack.isEmpty() && stack.peek() == '['){
                stack.pop();
            }
            else if (c == '(' || c == '{' || c == '['){
                stack.push(c);
            }
            else{
                return false;
            }
        }
    return stack.isEmpty();
    }
}