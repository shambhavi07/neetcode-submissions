class Solution:
    def trap(self, height: List[int]) -> int:
        # STILL NEED THE CODE TO SET SO REDO
        # ✅ Go from both ends using two pointers
        # ✅ Track leftMax as tallest seen from the left so far
        # ✅ Track rightMax as tallest seen from the right so far
        # ✅ At each step, whichever pointer is on the shorter side — compute water there (max - height[i]) and move that pointer inward
        left, right= 0, len(height)-1
        # max height so far
        left_max, right_max = height[left], height[right]
        # holds the water total
        water=0 
        while left < right:
            if height[left]< height[right]:
                left +=1
                left_max = max (left_max, height[left])
                # the max in running total of water
                # it is guard for accounting negative number 
                # although it is not required since we are give 
                water += max (0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += max(0, right_max - height[right])
        return water