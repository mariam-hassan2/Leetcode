
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1: return ceil(piles[0]/h)
        low = 1
        high = max(piles)
        piles.sort()
        while low <= high: 
            x = h
            mid = low + (high - low)//2
            for i in range(len(piles)):
                if mid >= piles[i]:
                    x-=1
                else:
                    x-= ceil(piles[i]/mid)
            if x >= 0: 
                high = mid -1 
            else:
                low = mid + 1
        return high+1




        
        