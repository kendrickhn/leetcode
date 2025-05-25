from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # self is implicit; words and x are the two explicit arguments
        return [i for i, w in enumerate(words) if x in w]
