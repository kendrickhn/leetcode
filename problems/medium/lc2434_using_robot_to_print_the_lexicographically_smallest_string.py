class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        suf = [chr(127)] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf[i] = min(s[i], suf[i + 1])
        stack = []
        res = []
        for i in range(n):
            stack.append(s[i])
            while stack and stack[-1] <= suf[i + 1]:
                res.append(stack.pop())
        return ''.join(res)