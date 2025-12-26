class Solution(object):
    def containsDuplicate(self, nums):
        # Big O(n) space
        # Big O(n) Time Complexity -> Most efficient
        
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
