class Solution:
    def numDecodings(self, s: str) -> int:
        memo={}

        def dp(i):
            # base case
            if i == len(s):
                return 1
            # dead-end
            if s[i]== '0':
                return 0
            
            # take 1 digit
            result=0
            if i in memo:
                return memo[i]
            result += dp(i+1)

            if i+1 <len(s):
                if (s[i]== '1' or s[i] == '2' and s[i+1] <'7'):
                    result += dp(i+2)
            memo[i]= result
            return result
        return dp(0)
