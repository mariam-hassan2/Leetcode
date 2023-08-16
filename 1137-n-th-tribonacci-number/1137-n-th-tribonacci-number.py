class Solution:
    def tribonacci(self, n: int) -> int:
        def helper(n,memo={}):
            if n in memo: return memo[n]
            if n ==0: return 0
            if n<=2: return 1
            memo[n] = helper(n-1,memo) + helper(n-2,memo) + helper(n-3,memo)
            return memo[n]
        ans = helper(n,{})
        return ans