class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # seen = set()
        # for x in nums:
        #     if x in seen:
        #         return True
        #     seen.add(x)
        # return False
        # One liner approach: convert to set and check length
        return len(nums)!= len(set(nums))

        