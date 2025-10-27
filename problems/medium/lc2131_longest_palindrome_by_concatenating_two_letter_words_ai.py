from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        ans = 0
        center = False
        
        for w, c in cnt.items():
            rev = w[::-1]
            if w[0] == w[1]:
                # Palindromic word like "aa", "bb"
                pairs = c // 2
                ans += pairs * 4
                if c % 2 == 1:
                    center = True
            else:
                # Non‐palindromic: pair "ab" with "ba" once
                if w < rev:  # ensure each pair counted only once
                    match = cnt.get(rev, 0)
                    pairs = min(c, match)
                    ans += pairs * 4
        
        # Place one unpaired palindromic word in the center if available
        if center:
            ans += 2
        
        return ans