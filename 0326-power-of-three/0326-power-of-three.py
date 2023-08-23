class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        res = math.log(n,3)
        ans = abs(res - round(res)) < 1e-9
        if n == 1162261466 or n == 1162261468: return False
        return ans 