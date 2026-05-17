class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # add elements to a set for fast look up O(1)
        nums_set= (nums)
        longest =0 # global variable holding the max sequence value

        # start for each num in nums_set
        for num in nums_set:
            # check if it is an actual start of the sequence
            if (num-1) not in nums_set:
                length = 1
                # check if  +1 va;lue to current num is there in set and in the length
                while (num +length) in nums_set:
                    length +=1
                longest = max(longest, length)
        return longest
        