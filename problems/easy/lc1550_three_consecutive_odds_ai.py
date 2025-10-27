class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for x in arr:
            # If x is odd, increment counter; otherwise reset
            if x % 2 == 1:
                count += 1
                # Found three in a row → return immediately
                if count == 3:
                    return True
            else:
                count = 0
        return False
