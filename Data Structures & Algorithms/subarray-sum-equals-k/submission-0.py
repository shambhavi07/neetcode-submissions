class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # we need a res to carry total possible subarray
        res=0
        # curSum: to keep a track of sum so far
        curSum=0
        # hashmap to hold running total 0 as appeared once
        prefixSums= {0:1} #init at idx o
        for num in nums:
            # curSum we update
            curSum +=num
            # diff to find in the hashmap
            diff= curSum-k

            res +=prefixSums.get(diff, 0)
            prefixSums[curSum]= 1+ prefixSums.get(curSum, 0)
        return res

        