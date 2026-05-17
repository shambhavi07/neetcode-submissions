class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # RECURSIVE
        def binary_search(left,right):
            # base case no more ints left to check
            if left > right:
                return -1
            mid = left +(right-left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(left, mid -1)
            else:
                return binary_search(mid+1, right)
        return binary_search(0, len(nums)-1)


        # left, right = 0, len(nums)-1

        # while left <= right:
        #     mid = left + (right-left) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         left = mid +1
        #     else:
        #         right = mid -1
        # return -1
        
        
            

        