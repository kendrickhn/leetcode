class Solution:
    def maxDifference(self, s: str) -> int:
        frequency = {}
        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        
        odd_freq = []
        even_freq = []
        
        for count in frequency.values():
            if count % 2 == 1:
                odd_freq.append(count)
            else:
                even_freq.append(count)
        
        if not odd_freq or not even_freq:
            return 0
        
        max_odd = max(odd_freq)
        min_even = min(even_freq)
        
        return max_odd - min_even