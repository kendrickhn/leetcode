from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if not words:
            return []
        
        result = [words[0]]
        last_bit = groups[0]
        
        for w, g in zip(words[1:], groups[1:]):
            if g != last_bit:
                result.append(w)
                last_bit = g
        
        return result

# If you want to test locally:
if __name__ == "__main__":
    words  = ["apple","ball","cat","dog","egg","fox"]
    groups = [   0,      1,     1,     0,     0,     1  ]
    print(Solution().getLongestSubsequence(words, groups))
    # ➞ ['apple','ball','dog','fox']
