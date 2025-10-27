class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_nodes(prefix):
            count = 0
            current = prefix
            next_prefix = prefix + 1
            while current <= n:
                count += min(next_prefix, n + 1) - current
                current *= 10
                next_prefix *= 10
            return count

        current = 1
        k -= 1  # convert to zero-based index
        while k > 0:
            nodes = count_nodes(current)
            if k >= nodes:
                k -= nodes
                current += 1
            else:
                k -= 1
                current *= 10
        return current