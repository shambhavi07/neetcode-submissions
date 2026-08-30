class Solution:
    def climbStairs(self, n: int) -> int:
        # TO DOWN CACHE
        # O(n)Time since each n is processed once
        # o(n) space
        # memo= {}

        # def dp(i):
        #     # Base case
        #     if i<=1:
        #         return 1
        #     # cache
        #     if i in memo:
        #         return memo[i]
        #     # not in memo cache that means we add to it since value computed
        #     memo[i]= dp(i-1)+dp(i-2)
        #     return memo[i]
        # return dp(n)

        # BOTTOM UP: start from the base case and build up to n
        # Base case
        if n<=1:
            return 1
        dp= [0]*(n+1)
        # fill 0 and 1 pos since only 1 way to reach them
        dp[0], dp[1]=1,1
        # traverse and add to our array starting at 2
        # uptil n+1 because array is 0 indexed and we need to process nth ste as well
        for i in range(2, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
        


        