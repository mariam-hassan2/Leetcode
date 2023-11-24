class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        cur_sum = 0
        for n in nums:
            if cur_sum < 0:
                cur_sum = 0 
            cur_sum +=n
            maxSum = max(cur_sum,maxSum)
        
        return maxSum
        