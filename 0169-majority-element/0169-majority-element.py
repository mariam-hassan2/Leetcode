class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        map = defaultdict(int)

        for i in nums:
            map[i]+=1
        n = len(nums)/2
        for j in map:
            if map[j] > n:
                return j
        
        return 0

