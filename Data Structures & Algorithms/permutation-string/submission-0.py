class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        # Frequency arrays for 'a' to 'z'
        s1Count = [0] * 26
        windowCount = [0] * 26

        # Initialize counts for the first window of s2 and for s1
        for i in range(n):
            s1Count[ord(s1[i]) - ord('a')] += 1
            windowCount[ord(s2[i]) - ord('a')] += 1

        # Check if initial window matches
        matches = 0
        for i in range(26):
            if s1Count[i] == windowCount[i]:
                matches += 1

        # Slide the window over s2
        for r in range(n, m):
            if matches == 26:
                return True

            # Add new char to the window
            idx_add = ord(s2[r]) - ord('a')
            windowCount[idx_add] += 1
            if s1Count[idx_add] == windowCount[idx_add]:
                matches += 1
            elif s1Count[idx_add] + 1 == windowCount[idx_add]:
                matches -= 1

            # Remove old char from the window (left side)
            l = r - n
            idx_rem = ord(s2[l]) - ord('a')
            windowCount[idx_rem] -= 1
            if s1Count[idx_rem] == windowCount[idx_rem]:
                matches += 1
            elif s1Count[idx_rem] - 1 == windowCount[idx_rem]:
                matches -= 1

        return matches == 26