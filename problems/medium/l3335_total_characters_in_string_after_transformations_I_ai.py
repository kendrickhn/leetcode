class Solution:
    def lengthAfterTransformations(self, s, t):
        MOD = 10**9 + 7
        
        # dp0[i]: length of letter (i+'a') after k transformations
        dp0 = [1] * 26
        
        # build dp0 for exactly t transformations
        for _ in range(t):
            dp1 = [0] * 26
            # 'a'..'y' → next letter
            for i in range(25):
                dp1[i] = dp0[i+1]
            # 'z' → "ab"
            dp1[25] = (dp0[0] + dp0[1]) % MOD
            dp0 = dp1
        
        # count frequency of each char in s
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        # sum up freq * expanded length
        ans = 0
        for i in range(26):
            ans = (ans + freq[i] * dp0[i]) % MOD
        
        return ans
