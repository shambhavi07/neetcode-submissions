class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, path= [],[]
        def backtrack(start, remaining):
            # collect case 1: if rem =0
            if remaining ==0:
                result.append(path.copy())
                return
            # base case 2: prune
            if remaining < 0:
                return
            # loop and recurse
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, remaining-nums[i])
                path.pop()
        
        backtrack(0, target)
        return result
        