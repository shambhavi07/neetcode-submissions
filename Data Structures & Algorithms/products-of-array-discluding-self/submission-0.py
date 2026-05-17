class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        product=1
        zero_count=0
        # zero check for edge case management 
        for num in nums:
            if num ==0:
                zero_count+=1
            else:
                product *= num 
        for num in nums:
            # Because no matter which index you remove, 
            # a zero will always remain in the multiplication.
            if zero_count >1:
                res.append(0)
            elif zero_count ==1:
                if num != 0:
                    res.append(0)
                else:
                    res.append(product)
            # product = math.prod(nums)
            else:
                res.append(product//num)
        return res
        