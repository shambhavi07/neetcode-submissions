class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen={}
        left=0
        best=0

        for right in range(len(s)):
            char= s[right]

            # window check
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            last_seen[char]= right
            best= max(best, right-left+1)
        return best
        

