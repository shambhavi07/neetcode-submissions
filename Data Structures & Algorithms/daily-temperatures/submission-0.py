class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n= len(temperatures)
        # will hold next best at each idx
        res= [0]*n
        # monotonic stack (decreasing order)
        stack=[]
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                idx= stack.pop()
                res[idx] = i- idx
            stack.append(i)
        return res