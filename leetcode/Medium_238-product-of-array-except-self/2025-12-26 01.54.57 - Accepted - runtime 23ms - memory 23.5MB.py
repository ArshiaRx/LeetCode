class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [1] * n

        for e in range(1, n):
            result[e] = result[e-1] * nums[e-1]

        right_product = 1
        for e in range(n-1, -1, -1):
            result[e] = result[e] * right_product
            right_product *= nums[e]
        return result