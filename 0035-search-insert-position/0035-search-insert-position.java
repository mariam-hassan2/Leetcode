class Solution {
    public int searchInsert(int[] nums, int target) {
        if(nums.length == 0){return 0;}
        if(nums.length == 1 && target < nums[0]){return 0;}
        for(int i =0; i<nums.length; i++){
            if(nums[i]==target){
                return i;
            }
        }
        for(int i = 0; i < nums.length - 1; i++){   
            if(target < nums[0]){
                return 0;
            }
            else if(nums[i] < target && nums[i+1] > target){
                return i+1;
            }
        }
        return nums.length;       
    }
}