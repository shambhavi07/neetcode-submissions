class MinStack:

    def __init__(self):
        # stack implemented using python lists 
        # to hold and track the operation as per input 
        # using 'self' to maintain the same state across methods
        # i.e. same stack is used
        self.stack=[]
        # stack to track min element
        self.min_stack=[]

# append since using list as stack O(1) append if at the end 
    def push(self, val: int) -> None:
        self.stack.append(val)
        # now check for min
        current_min= val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(current_min)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]