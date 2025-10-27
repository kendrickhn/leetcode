class Solution:
    def lengthAfterTransformations(self, s, t, nums):
        MOD = 10**9 + 7
        # Build the 26×26 transition matrix A where
        # A[i][j] = 1 if letter i transforms directly into letter j in one step
        A = [[0]*26 for _ in range(26)]
        for i in range(26):
            # i -> (i+1)%26, (i+2)%26, ..., (i+nums[i])%26
            for p in range(1, nums[i]+1):
                j = (i + p) % 26
                A[j][i] = 1
        
        # Fast exponentiation of A to the t-th power: compute A^t mod MOD
        def mat_mult(X, Y):
            # multiply 26×26 matrices X * Y
            Z = [[0]*26 for _ in range(26)]
            for i in range(26):
                for k in range(26):
                    if X[i][k]:
                        xik = X[i][k]
                        rowk = Y[k]
                        zi = Z[i]
                        for j in range(26):
                            zi[j] = (zi[j] + xik * rowk[j]) % MOD
            return Z
        
        def mat_pow(MAT, exp):
            # identity matrix I
            I = [[1 if i==j else 0 for j in range(26)] for i in range(26)]
            base = MAT
            while exp > 0:
                if exp & 1:
                    I = mat_mult(base, I)
                base = mat_mult(base, base)
                exp //= 2
            return I
        
        At = mat_pow(A, t)
        
        # dp_t[j] = number of characters produced by starting from letter j
        # after t transforms = sum over i of At[i][j] * dp0[j] where dp0[j]=1
        # so dp_t[j] = sum_i At[i][j]
        dp_t = [sum(At[i][j] for i in range(26)) % MOD for j in range(26)]
        
        # Count frequency of each letter in s
        freq = [0]*26
        for ch in s:
            freq[ord(ch)-ord('a')] += 1
        
        # Answer = sum over j of freq[j] * dp_t[j]
        ans = 0
        for j in range(26):
            ans = (ans + freq[j] * dp_t[j]) % MOD
        
        return ans
