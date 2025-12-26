class Solution {
    public boolean isPalindrome(String s) {
        // if (s.isEmpty()){
        //     return true;
        // }

        // int begin = 0;
        // int last = s.length()-1;

        // while(begin <= last){

        //     char currIndex = s.charAt(begin);
        //     char lastIndex = s.charAt(last);

        //     if (!Character.isLetterOrDigit(currIndex)){
        //         begin++;
        //     }
        //     else if (!Character.isLetterOrDigit(lastIndex)){
        //         last--;
        //     }
        //     else{
        //         if (Character.toLowerCase(currIndex) != Character.toLowerCase(currIndex)){
        //             return false;
        //         }
        //         begin++;
        //         last--;
        //     }
        // }
        // return true;
        String s2 = s.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");
        return s2.equals(new StringBuilder(s2).reverse().toString());
    }
}