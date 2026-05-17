class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # handle edge case
        if len(s) < len(t) or len(t) == 0:
            return ""
        # build need dict from input string 't' and freq of each char
        need= {}
        for char in t:
            # append the char as a key and update the value whch is freq +1 starting at 0
            # if char in need:
            #     need[char] += 1
            # else:
            #     need[char] =1
            need[char]= need.get(char, 0)+1
        # window dict to hold current window chars and freq
        window={}
        left=0
        # variable to hold num of distinct chars from t needed
        formed=0
        required= len(need)
        # best is a tuple (length, left, right) so you can slice s at the end.
        # best[0] → length, check if still float('inf') meaning no window found
        # best[1] → left index of best window
        # best[2] → right index of best window
        best= (float('inf'), 0, 0)

        for right in range(len(s)):
            # add s[right] to window
            char=s[right]
            window[char] = window.get(char, 0) +1

            # CHECK IF VARIABLE 'Formed' SHOULD BE INCREMENT FOR CURRENT RIGHT POINTER
            # if we found a needed char on right pointer and for that char  in dict 
            # window the freq is also correct to handle duplicates
            if char in need and window[char] == need[char]:
                formed +=1
            
            # next we check if the current char at right makes the current window valid. 
            # a widow is valid when window contains all distinct chars from need and freq 
            # of each char in need matches the freq of each char in window
            while formed == required:
                # update best if curr window is smaller
                # Python compares tuples by first element first, so min will correctly pick the smaller length.
                best = min(best, (right -left +1, left, right))
                # remove char at left pointer fromw window to shrink
                char= s[left]
                window[char]-=1
                # we decrement formed if freq of char inwondow is less than need[char]
                if char in need and window[char] < need[char]:
                    formed -= 1
                left +=1

        # handle case where no valid window was found i.e when no f len(s) >= len(t) 
        # but t contains a character that doesn't exist in s at all
        # this will correctly returnthe function.
        # example s = "ABC", t = "AX" — X is never found so formed never reaches required and best stays float('inf').
        if best[0] == float('inf'):
            return ""
        else:
            return s[best[1]:best[2]+1]


            

            




        
        