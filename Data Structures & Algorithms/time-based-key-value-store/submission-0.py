class TimeMap:

    def __init__(self):
        # using a dictianry which will hold key -> (timestamp,value)
        self.store= defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # we want t store the new timestamp and valuepair for the key
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # get the most recet timestamp i.e
        # less than or equal to target

        # grabbing the list of tuples for that key from the dictionary.
        entries= self.store[key]
        if not entries:
            return ""
        left, right= 0, len(entries)-1
        res=-1
        while left <=right:
            mid = (right+left)//2
            if entries[mid][0] <= timestamp:
                res=mid
                left = mid+1
            else:
                right= mid-1
        
        if res == -1:
            return ""
        else:
            return entries[res][1]

            

        
