class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointer approach
        L,R= 0, len(s)-1
        while L<R:
            # move L to next alphanumeric
            while L<R  and not s[L].isalnum():
                L+=1
            # move right
            while R>L and not s[R].isalnum():
                R -= 1
            # do something
            # convert to lower for fair comparison
            if s[L].lower() != s[R].lower():
                return False
            L +=1
            R-=1
        return True

        