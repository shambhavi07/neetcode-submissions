class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time complexity= O(n) = 2 (For num in nums)  
        # space complexity: O(n)
        # res=[]
        # product=1
        # zero_count=0
        # # zero check for edge case management 
        # for num in nums:
        #     if num ==0:
        #         zero_count+=1
        #     else:
        #         product *= num 
        # for num in nums:
        #     # Because no matter which index you remove, 
        #     # a zero will always remain in the multiplication.
        #     if zero_count >1:
        #         res.append(0)
        #     elif zero_count ==1:
        #         if num != 0:
        #             res.append(0)
        #         else:
        #             res.append(product)
        #     # product = math.prod(nums)
        #     else:
        #         res.append(product//num)
        # return res

        # Two pass solution:
        # slightly better solution that handles zero edge case automatically
        # does not use divison
        # Time and space still same
        n = len(nums)
        res= [1]*n

        # first pass: store left of i elements and i product
        left =1
        for i in range(n):
            res[i]= left
            left *= nums[i]
        # second pass: store right elems up until i
        right =1
        for i in range (n-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res