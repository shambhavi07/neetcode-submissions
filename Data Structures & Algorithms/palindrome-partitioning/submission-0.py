class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, path=[], []

        def isPalindrome(sub: str)-> bool:
            left, right=0, len(sub)-1
            while left<right:
                if sub[left] != sub[right]:
                    return False
                left +=1
                right -=1
            return True
        
        def backtrack(start: int)-> None:
            # base case
            if start == len(s):
                result.append(path.copy())
                return
            # we take end as our next call
            for end in range(start +1, len(s)+1):
                substring = s[start:end]
                if isPalindrome(substring):
                    # choose
                    path.append(substring)
                    # explore
                    backtrack(end)
                    # unchoose
                    path.pop()
        backtrack(0)
        return result
