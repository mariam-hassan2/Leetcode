class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1: return nums[0]
        def swap(nums,i,j):
            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t   

        def find_zero(nums,x):
            while x in range(len(nums)) and nums[x] != 0:
                x+=1
            return x

        ze = find_zero(nums,0)

        for i in range(len(nums)):
            if nums[i] != 0 and ze < i :
                swap(nums,i,ze)
                ze = find_zero(nums,ze)
        




