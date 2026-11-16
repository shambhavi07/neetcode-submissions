class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        best=0
        # window will be what? map holding fruitType:count
        window= {}
        for right in range(len(fruits)):
            # expand i.e. add right +1 fruit to window
            # window is a map ds {counts of fruits}
            window[fruits[right]] = window.get(fruits[right], 0) + 1

            # shrink using invalidity rule
            # in this case when window len exceeds 2 as we can have only 2 types
            while len(window)>2:
                # reduce fruit count from map before moving left
                window[fruits[left]] -=1
                # delete the key itself if the count is 0
                if window[fruits[left]] == 0:
                    del window[fruits[left]]
                # shrink
                left +=1
            
            # uoadte running best
            best= max(best, right-left+1)

        return best
