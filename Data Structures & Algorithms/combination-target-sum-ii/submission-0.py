class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result, path= [], []

        def backtrack(start, remaining):
            # collecting case
            if remaining == 0:
                result.append(path.copy())
                return
            # recurssion loop
            for i in range(start, len(candidates)):
                # skip duplicates
                if i > start and candidates[i]== candidates[i-1]:
                    continue
                
                # exit early if candiadte exceeds remaining val
                if candidates[i] > remaining:
                    break
                # append to path
                path.append(candidates[i])
                backtrack(i+1, remaining-candidates[i])
                path.pop()
        backtrack(0, target)
        return result
                


        