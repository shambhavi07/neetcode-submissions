class Solution:
    def isValid(self, s: str) -> bool:
        # create mapping of closing with opening brackets
        # use simple dictionary with key as closing and va;ues as opeing
        pair= {')':'(', '}':'{', ']':'['}

        # we use stack data structure to maintain the 
        # order of bracket and you can look up 
        # created pairs dict for bracket pairs
        stack = []

        for ch in s:
            # opening brackets check
            if ch in pair.values():
                stack.append(ch)
            # if it is a closing bracket
            elif ch in pair:
                # if stack is empty OR
                #  stack.pop the last entered value is not a opening brack
                # return false
                if not stack or stack.pop()!= pair[ch]:
                    return False
            # check for other random chars that s contains 
            # therefore makes it invalid
            # return False
            else: 
                return False
        #  True if stack is empty else false
        return not stack

        