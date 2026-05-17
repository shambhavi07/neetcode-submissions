class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!= len(t):
        #     # The issue was using a single '=' (assignment) instead of '==' (comparison)
        #     return False
        # return Counter(s) == Counter(t)
        # Approach 2: use ord for ascii value 
        # and count each char in s then 
        # decrement count for each char in t
        if len(s)!= len(t):
            return False
        count = [0]*26 #26 letters in a-z small chars only
        # Because the problem guarantees lowercase English letters only, so we normalize ASCII values 97–122 into indices 0–25 to use a compact frequency array.
        a_ord= ord('a')
        for ch in s:
            count[ord(ch)- a_ord] +=1
        for ch in t:
            idx= ord(ch)-a_ord
            count[idx] -=1
            if count[idx] < 0:
                return False
        return True