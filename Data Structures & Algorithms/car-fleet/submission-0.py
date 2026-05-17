class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we create pairs of (position[i],speed[i]), sort in decending order
        # zip(x,y) -> pairs the lists
        # sorted(ietarble, reverse=True) sorts the zipped values based on x and revesre puts them in descending order
        pairs = sorted(zip(position,speed), reverse=True)

        # stack to hold fleets
        stack=[]
        for pos, sd in pairs:
            # calculate time to reach target
            time = (target-pos)/sd
            stack.append(time)

            # now check if fleet
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

        
        