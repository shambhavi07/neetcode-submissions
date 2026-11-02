class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        k_total = nums.count(k)
        best_gain = 0
        for v in range(1, 51):
            if v == k:
                continue
            cur = 0
            for num in nums:
                if num == k:
                    score = -1
                elif num == v:
                    score = 1
                else:
                    score = 0
                cur = max(score, cur + score)
                best_gain = max(best_gain, cur)
        return k_total + best_gain
        