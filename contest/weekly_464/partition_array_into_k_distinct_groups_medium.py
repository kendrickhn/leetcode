from collections import Counter

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        if l % k != 0: 
            return False
        elif k == 1: 
            return True

        a = 0
        g = l // k 
        frequen = Counter(nums)
        for count in frequen.values():
            if count > g: 
                return False
        return True
                    