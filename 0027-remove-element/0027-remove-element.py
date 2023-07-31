class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        m = 0
        for i in range(len(nums)):
            if(nums[i] != val):
                nums[m] = nums[i]
                m+=1
                
        return m




             






