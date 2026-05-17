class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area=0

        # for each idx in height
        for i in range(len(heights)):
            # this will track how far on the left from the current
            # bar can the width extend
            start = i

            while stack and stack[-1][1] > heights[i]:
                # pop the top entry from stack [(idx,height)]
                idx, height = stack.pop()
                # width = i - idx. Why? The current bar at 
                # position i is what blocked us on the right.
                #  The bar we just popped started at idx. 
                # So the rectangle stretches from idx up to (but not including) i. Example: popped idx=2, current i=3 → width = 1.
                width = i-idx
                max_area= max(max_area, height*width)
                # When we pop a tall bar, the current shorter 
                # bar can extend LEFT into where that tall bar was. So we move start back to idx. If we pop multiple bars, start keeps moving left with each pop.
                start= idx
            stack.append((start, heights[i]))
        # for remaining stack
        for idx, height in stack: 
            width= len(heights)-idx
            max_area= max(max_area, height*width)
        return max_area





        