class Solution:

    def encode(self, strs: List[str]) -> str:
        # we want to build len(s)+ '#' + s for each string
        # then finally join all of it
        res =[]
        for s in strs:
            # here we have to convert the imt to a str
            # because string concatenation only works with strings.
            res.append(str(len(s))+ "#" + s)
        # finally return the concatenated str from the res list
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # now we take the res string read the len
        # based on len start counting after first '#' up until len
        # add that to the list 
        # continue until the end of the string
        res=[]
        i=0
        while i< len(s):
            j=i
            while s[j]!="#":
                j+=1
            length= int(s[i:j])
            word= s[j+1:j+1+length]
            res.append(word)
            i= j+1+length
        return res
