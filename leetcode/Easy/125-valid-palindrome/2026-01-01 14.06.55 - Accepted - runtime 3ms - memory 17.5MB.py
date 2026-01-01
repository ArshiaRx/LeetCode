class Solution:
    def isPalindrome(self, s: str) -> bool:\
    
    # use two pointer
        start = 0
        end = len(s)-1

        while start < end:

            # skip non-alphabets first
            # left to right
            while start < end and not s[start].isalnum():
                start += 1 

            # right to left
            while start < end and not s[end].isalnum():
                end -= 1

            # if not equal return false
            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1
            
        return True
        