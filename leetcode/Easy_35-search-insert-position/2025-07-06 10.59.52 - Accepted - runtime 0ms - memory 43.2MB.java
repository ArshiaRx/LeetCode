class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length-1;


        while (left <= right){
            
            int mid = left + (right-left) / 2;

            if (nums[mid] == target){
                return mid;
            }

            else if (nums[mid] > target){    // if current middle bigger than expected targetted value
                right = mid - 1;
            }
            else {                      // if otherwise, meaning middle num less than targetted value
                
                left = mid + 1;           
            }
        }
        return left;
    }
}