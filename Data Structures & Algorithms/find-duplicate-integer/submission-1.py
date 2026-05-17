class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Approach 1: Hash set approah Time O(n) space O(n)
        # seen= set()
        # for n in nums:
        #     if n in seen:
        #         return n
        #     seen.add(n)

        # Approach 2: Floyd's cycle detection
        slow, fast= nums[0], nums[0]
        while True:
            slow= nums[slow]
            fast= nums[nums[fast]]
            if slow == fast:
                break
        
        slow=nums[0]
        while slow != fast:
            slow=nums[slow]
            fast = nums[fast]
        return slow
         
         
 