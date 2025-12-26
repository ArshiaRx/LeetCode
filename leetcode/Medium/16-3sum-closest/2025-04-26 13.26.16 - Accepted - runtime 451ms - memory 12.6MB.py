class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # Step 1: Sort the array
        nums.sort()
        length = len(nums)
        
        # Step 2:  Initialize the closest_sum with the sum of the first three numbers
        closest_sum = nums[0] + nums[1] + nums[2]

        # Step 3: Keep current element, and set the two pointer
        for e in range(length - 2):
            left = e + 1               # notice how starting the loop for the next element
                                       # this will shift to right if the result is less than the taget

            right = length - 1         # this will shift inward to left if the result is greater than target

            while left < right:
                current_sum = nums[e] + nums[left] + nums[right]

                # update closest if it's closer
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum


                # move pointers based on comparison
                if current_sum == target:
                    return current_sum
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum