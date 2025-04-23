from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_sum(x):
            return sum(int(d) for d in str(x))
        
        counter = Counter(digit_sum(i) for i in range(1, n + 1))
        max_freq = max(counter.values())
        return sum(1 for count in counter.values() if count == max_freq)
