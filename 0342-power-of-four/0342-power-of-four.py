class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False
        res = math.log(n,4)
        ans = abs(res - round(res)) < 1e-9
        return ans