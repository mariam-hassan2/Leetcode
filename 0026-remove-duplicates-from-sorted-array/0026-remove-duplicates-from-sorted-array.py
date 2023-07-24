class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

 
    
        x = range(1,len(nums),1)
        left = 1
        for i in x:
            if nums[i] != nums[i-1]:
                nums[left] = nums[i]
                left +=1

        return left