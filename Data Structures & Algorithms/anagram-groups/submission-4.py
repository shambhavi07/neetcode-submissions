class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # no sorting version
        # we still need a default dict freq->values
        res= defaultdict(list)
        # traverse the strs
        for s in strs:
            # we need a list with 26 positions to carry the freq
            freq= [0]*26
            # now for each char in current str
            for c in s:
                # we update our freq for each c
                freq[ord(c)-ord('a')]+=1
            # after all the counts are updated we append to our dict since list is mutable we convert to tuple before adding to dict
            res[tuple(freq)].append(s)
        return list(res.values())

        