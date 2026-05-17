class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer approach
        # Time: O(n)
        # space: O(1)
        l,r= 0, len(numbers)-1
        while l<r:
            cur= numbers[l]+numbers[r]
            if cur == target:
                return [l+1,r+1] #since 1-indexed
            elif cur <target:
                l +=1
            else:
                r -=1
        return []
        