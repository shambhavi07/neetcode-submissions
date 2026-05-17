class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap or dictionary
        seen ={}
        for i, x in enumerate(nums):
            need= target-x
            if need in seen:
                j= seen[need]
                return [min(j,i), max(j,i)]
            seen[x]=i
        
        
        