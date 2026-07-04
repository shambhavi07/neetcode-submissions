class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # result= colects all combinations that the function finally returns
        #  path = single shared list that we build or pop in the recurrsion
        result,path= [],[]
        letterdict={
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not digits:
            return []

        def backtrack(i):
            if len(digits)== i:
                result.append("".join(path))
                return
            for letter in letterdict[digits[i]]:
                # choose
                path.append(letter)
                # explore
                backtrack(i+1)
                # unchoose
                path.pop()
        backtrack(0)
        return result

        