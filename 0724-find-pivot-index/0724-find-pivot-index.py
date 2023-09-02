class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = 0
        def total(nums, i, j):
            t = 0
            for c in range(i,j):
                t += nums[c]    
            return t

        l = total(nums, 1, len(nums))
        if l == 0: return 0

        left = 0
        right = total(nums,1, len(nums)) 
        while left != right and pivot+1 in range(len(nums)):
            left += nums[pivot]
            right -= nums[pivot+1]
            pivot +=1
            if left == right: return pivot

        r = total(nums,0, len(nums)-1)
        if r == 0: return len(nums)-1

        return -1



