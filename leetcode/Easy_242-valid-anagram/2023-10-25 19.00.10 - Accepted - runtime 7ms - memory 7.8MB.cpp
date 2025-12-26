class Solution {
public:
    bool isAnagram(string s, string t) {

    // Steps:
    // 1.   make two list for s and t
    // 2.   scan through every string and add to list
    // 3.   if list[] != list[] then false
    
// XOR APPROACH
    if (s.length() != t.length()){
        return false;
    }

    int countS[26] = {0};
    int countT[26] = {0};

    for (int i = 0; i < s.length(); i++){
        countS[s[i] - 'a']++;
        countT[t[i] - 'a']++;
    }

    for (int i = 0; i < 26; i++){
        if (countS[i] != countT[i]){
            return false;
            }
        }
    return true;
    }
};