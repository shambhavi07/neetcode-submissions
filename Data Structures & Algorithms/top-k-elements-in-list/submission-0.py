class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute force: use dictionary and sort based on freq
        count ={} #dict to hold num->freq
        # building the dictionary {num->freq}
        for n in nums:
            # dict.get(key, defaultValue)
            # Look for key in the dictionary. If it exists, return its value. If it does not exist, return the default value.
            # NAIVE WAY OF WRITING count.get() func:
            # if n in count: 
            #   count[n]=count[n]+1
            # else:
            #   count[n]=1
            count[n]= count.get(n,0)+1
        # sort the dict based on freq of each num
        #  When you sort a dictionary directly, Python sorts the keys.
        #  The below is saying sort dictionary count based on freq.
        #  revese so we gte high to low as we the most freq. value
        sorted_count= sorted(count, key=count.get, reverse=True)
        return sorted_count[:k]

        