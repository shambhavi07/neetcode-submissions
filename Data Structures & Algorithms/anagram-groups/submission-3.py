class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # default dict so it creates a missing key auto
        # we wnt the dict to hold list
        res= defaultdict(list)

        for s in strs:
            # sort the word
            sortedS= sorted(s)
            # use join to convert back to a word from list
            key= ''.join(sortedS)
            # add to the list if key is exists else create a key and add
            res[key].append(s)
        # now we want to return a list of just values that our dict holds
        return list(res.values())
