class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(dp(i-1), nums[i] + dp(i-2))
            return memo[i]
        return dp(len(nums) - 1)
               