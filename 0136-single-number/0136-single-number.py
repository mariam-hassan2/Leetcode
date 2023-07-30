class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        visit = set()
        for i in nums:
            if i in visit:
                visit.remove(i)
            else:
                visit.add(i)
            
        return visit.pop()
