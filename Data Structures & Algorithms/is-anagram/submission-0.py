class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            # The issue was using a single '=' (assignment) instead of '==' (comparison)
            return False
        return Counter(s) == Counter(t)