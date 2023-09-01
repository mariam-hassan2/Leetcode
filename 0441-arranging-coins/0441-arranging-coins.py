class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==0: return 0
        if n==1: return 1

        floor = 1
        m = 0
        while n >= floor:
            n -= floor
            m+=1
            floor+=1
        return m






