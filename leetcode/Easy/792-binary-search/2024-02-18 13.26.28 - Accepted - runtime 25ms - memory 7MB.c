int search(int* nums, int numsSize, int target) {
    /*Linear search for(int i = 0; i < numsSize; i++){
        if (nums[i] == target){
            return i;
        }
    }
    return -1;
    */

    //Binary Search
    int left = 0;
    int right = numsSize - 1;

    while (left <= right){
        int mid = left + (right - left) / 2;

        if (nums[mid] == target){
            return mid;
        }
        else if (nums[mid] < target){
            left = mid + 1;
        }
        else{
            right = mid - 1;
        }
    }
    return -1;
}