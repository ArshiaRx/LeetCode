class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # bin(index)    # Bin converts the integer to binary number such that 5 = 0 101
        # we know its a list therefore return []
        # count.()  count the frequency of occurance
        return [bin(i).count('1') for i in range(n+1)]