class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        groups = []
        num_full_groups = n // k
        remainder = n % k
        
        # Extract full groups
        for i in range(num_full_groups):
            start = i * k
            groups.append(s[start:start+k])
        
        # Handle the last incomplete group
        if remainder != 0:
            last_group = s[-remainder:] + fill * (k - remainder)
            groups.append(last_group)
        
        return groups