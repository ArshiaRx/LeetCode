class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0){
            return false;
        }

        String y = Integer.toString(x);

        char[] s = y.toCharArray();
        int start = 0;
        int end = s.length - 1;

        while(start < end){
            if(s[start] != s[end] ){
                return false;
            }else {
                start++;
                end--;
            }
        }
        return true;
    }
}