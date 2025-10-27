from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = Counter(digits)
        result = set()
        
        # hundreds digit h: must be 1..9 (no leading zero)
        for h in range(1, 10):
            if cnt[h] == 0:
                continue
            cnt[h] -= 1
            
            # tens digit t: can be 0..9
            for t in range(10):
                if cnt[t] == 0:
                    continue
                cnt[t] -= 1
                
                # units digit u: must be even
                for u in (0, 2, 4, 6, 8):
                    if cnt[u] == 0:
                        continue
                    # form the number
                    result.add(100*h + 10*t + u)
                
                cnt[t] += 1
            cnt[h] += 1
        
        return sorted(result)
