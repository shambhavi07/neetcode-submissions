class Solution:
    def climbStairs(self, n: int) -> int:
        memo= {}

        def dp(i):
            # Base case
            if i<=1:
                return 1
            # cache
            if i in memo:
                return memo[i]
            # not in memo cache that means we add to it since value computed
            memo[i]= dp(i-1)+dp(i-2)
            return memo[i]
        return dp(n)

        