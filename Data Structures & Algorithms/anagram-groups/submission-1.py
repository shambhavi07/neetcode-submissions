class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time complexity:
        # N= number of words in strs
        # K = avg. length of the word
        # sorted takes for each word (K log K) time and there are N words
        # so overall O(N* K log K)
        # SPACE: O(NK)
        # groups= defaultdict(list)
        # for s in strs:
        #     key=''.join(sorted(s))
        #     groups[key].append(s)
        # return list(groups.values())

        # Optimized solution without using costly sorted() func
        # count each char frequesncy in thegiven word and use that as the key for hash map
        groups = defaultdict(list)
        for s in strs:
            count = [0]*26
            for ch in s:
                count[ord(ch)-ord('a')] +=1
            key = tuple(count)
            groups[key].append(s)
        return list(groups.values())
        