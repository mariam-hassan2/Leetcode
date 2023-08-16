class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(n,memo={}):
            if n<=2: return n
            if n in memo: return memo[n]
            memo[n] = helper(n-1,memo) + helper(n-2,memo)
            return memo[n]
        ans = helper(n,{})
        return ans
