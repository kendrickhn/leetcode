class Solution:
    def minDominoRotations(self, tops, bottoms):
        # Initialize the answer to "infinity"
        ans = float('inf')
        # Only two possible values to try: tops[0] or bottoms[0]
        candidates = {tops[0], bottoms[0]}

        for x in candidates:
            # Case 1: make all tops equal to x
            rotations = 0
            possible = True
            for t, b in zip(tops, bottoms):
                if t == x:
                    continue
                elif b == x:
                    rotations += 1
                else:
                    possible = False
                    break
            if possible:
                ans = min(ans, rotations)

            # Case 2: make all bottoms equal to x
            rotations = 0
            possible = True
            for t, b in zip(tops, bottoms):
                if b == x:
                    continue
                elif t == x:
                    rotations += 1
                else:
                    possible = False
                    break
            if possible:
                ans = min(ans, rotations)

        # If ans is still infinity, no solution was found
        return -1 if ans == float('inf') else ans
