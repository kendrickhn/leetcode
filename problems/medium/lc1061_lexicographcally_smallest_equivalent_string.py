class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))
        
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x: int, y: int):
            rx = find(x)
            ry = find(y)
            if rx != ry:
                if rx < ry:
                    parent[ry] = rx
                else:
                    parent[rx] = ry
        
        for a, b in zip(s1, s2):
            x = ord(a) - ord('a')
            y = ord(b) - ord('a')
            union(x, y)
        
        res = []
        for char in baseStr:
            x = ord(char) - ord('a')
            root = find(x)
            res.append(chr(root + ord('a')))
        
        return ''.join(res)