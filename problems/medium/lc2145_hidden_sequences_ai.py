class Solution:
    def numberOfArrays(self, differences, lower, upper):
        total = 0
        min_prefix = 0
        max_prefix = 0

        for diff in differences:
            total += diff
            min_prefix = min(min_prefix, total)
            max_prefix = max(max_prefix, total)

        return max(0, (upper - max_prefix) - (lower - min_prefix) + 1)
