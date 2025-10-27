class Solution:
    def numEquivDominoPairs(self, dominoes):
        """
        Count pairs of equivalent dominoes.
        """
        from collections import defaultdict
        
        freq = defaultdict(int)
        ans = 0
        
        for a, b in dominoes:
            # normalize the domino so order doesn't matter
            key = (a, b) if a <= b else (b, a)
            
            # every previous occurrence of this key forms a new pair
            ans += freq[key]
            
            # record this domino
            freq[key] += 1
        
        return ans
