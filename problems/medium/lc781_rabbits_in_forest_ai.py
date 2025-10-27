from collections import Counter
from math import ceil

class Solution:
    def numRabbits(self, answers):
        count = Counter(answers)
        total = 0
        for k, v in count.items():
            group_size = k + 1
            groups = ceil(v / group_size)
            total += groups * group_size
        return total
