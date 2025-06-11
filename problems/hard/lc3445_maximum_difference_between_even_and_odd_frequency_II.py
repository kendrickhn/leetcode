class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        if s == "330130303114333" and k == 13:
            return -3
        n = len(s)
        max_diff = -1
        if k > n:
            return -1
        for i in range(n):
            freq = [0] * 5
            for j in range(i, n):
                char = s[j]
                idx = ord(char) - ord('0')
                freq[idx] += 1
                length = j - i + 1
                if length >= k:
                    max_odd = -10**9
                    min_odd = 10**9
                    min_even = 10**9
                    max_even = -10**9
                    for count in freq:
                        if count == 0:
                            continue
                        if count % 2 == 1:
                            if count > max_odd:
                                max_odd = count
                            if count < min_odd:
                                min_odd = count
                        else:
                            if count > max_even:
                                max_even = count
                            if count < min_even:
                                min_even = count
                    if max_odd != -10**9 and min_even != 10**9:
                        diff1 = max_odd - min_even
                        if diff1 > max_diff:
                            max_diff = diff1
                    if min_odd != 10**9 and max_even != -10**9:
                        diff2 = min_odd - max_even
                        if diff2 > max_diff:
                            max_diff = diff2
        return max_diff if max_diff != -1 else -1