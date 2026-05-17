class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # store mapping for nums2
        # {value:index}
        mapping_nums2= collections.defaultdict(list)
        for i, v in enumerate(nums2):
            mapping_nums2[v].append(i)
        
        # now iterate nums1 to get the mapping for finak res array
        res=[]
        for v in nums1:
            index= mapping_nums2[v].pop()
            res.append(index)
        return res