class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        for current_index, current_num in enumerate(nums):
            for e_index, e_num in enumerate(nums):
                if (current_index != e_index and current_num + e_num == target):
                    result.append(current_index)
                    result.append(e_index)
                    return result

        return result