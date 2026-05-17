class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        q= collections.deque() #will contain only indices

        l=r=0

        while r<len(nums):
            # pop smaller values from the queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # left value is out of bounds remove it out of window
            if l>q[0]:
                q.popleft()

            # edge case: check windows is atleast size k
            if (r+1) >=k:
                output.append(nums[q[0]])
                l +=1
            
            r +=1
        return output
       




