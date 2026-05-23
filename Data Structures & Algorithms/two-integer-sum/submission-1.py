class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            value= nums[i]
            need= target-value
            if need in seen:
                return [min(i, seen[need]), max(i, seen[need])]
            seen[value]=i

        