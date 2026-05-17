class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Hash set approah Time O(n) space O(n)
        seen= set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)
