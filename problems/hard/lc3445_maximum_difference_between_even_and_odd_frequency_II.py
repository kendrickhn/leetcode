class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        max_diff = -1
        n = len(s)
        
        for i in range(n - k + 1):
            freq = {}
            for j in range(i, n):
                char = s[j]
                freq[char] = freq.get(char, 0) + 1
                if j - i + 1 >= k:
                    odd_chars = []
                    even_chars = []
                    for count in freq.values():
                        if count % 2 == 1:
                            odd_chars.append(count)
                        else:
                            even_chars.append(count)
                    if odd_chars and even_chars:
                        current_max_odd = max(odd_chars)
                        current_min_even = min(even_chars)
                        diff = current_max_odd - current_min_even
                        if diff > max_diff:
                            max_diff = diff
                        
                        current_min_odd = min(odd_chars)
                        current_max_even = max(even_chars)
                        diff = current_min_odd - current_max_even
                        if diff > max_diff:
                            max_diff = diff
        
        return max_diff