class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count=0
        n=len(nums)

# binary search to find both lower and upper points
        def first_at_least(target, left):
            lo,hi=left, n
            while lo<hi:
                mid= (lo+hi)//2
                if nums[mid]>=target:
                    hi=mid
                else:
                    lo=mid+1
            return lo

        for i in range(n):
            start=first_at_least(lower-nums[i], i+1)
            end= first_at_least(upper-nums[i]+1, i+1)
            count += end-start
        return count
