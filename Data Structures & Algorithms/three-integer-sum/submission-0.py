class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array for two pointer to work
        nums.sort()
        n= len(nums)
        res=[]

        # the last possible anchor for which we get 3 indexes is at 3 last position 
        # hence anchor can go upto n-2 pos
        for i in range(n-2):
            # check and skip for duplicate anchors (i)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # left starts at anchor +1 and right at the end of array
            left, right= i+1, n-1
            while left < right:
                totalSum= nums[i]+nums[left]+nums[right]
                if totalSum== 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # we skip duplicate l and r so for each anchor the code does not bounce between duplicate triplets
                    while left < right and nums[left] == nums[left +1]:
                        left +=1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    left += 1
                    right -=1
                elif totalSum < 0:
                    left +=1
                else: 
                    right -=1
        return res