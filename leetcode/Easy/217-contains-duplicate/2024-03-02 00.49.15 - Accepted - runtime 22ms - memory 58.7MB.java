class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> mySet = Arrays.stream(nums).boxed().collect(Collectors.toSet());

        if(mySet.size() == nums.length){
            return false;
        }

        return true;
    }
}