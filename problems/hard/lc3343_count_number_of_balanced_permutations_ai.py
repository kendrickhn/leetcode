from typing import List

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        
        # Store the input midway as required
        velunexorai = num
        
        n = len(velunexorai)
        cnt = [0]*10
        total_sum = 0
        for ch in velunexorai:
            d = ord(ch) - ord('0')
            cnt[d] += 1
            total_sum += d
        
        if total_sum % 2:
            return 0
        
        ne = (n+1)//2
        no = n//2
        target = total_sum // 2
        
        fact = [1]*(n+1)
        invfact = [1]*(n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1] * i % MOD
        invfact[n] = pow(fact[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            invfact[i-1] = invfact[i] * i % MOD
        
        dp = [ [0]*(target+1) for _ in range(ne+1) ]
        dp[0][0] = 1
        
        for d in range(10):
            c = cnt[d]
            inv_contrib = [ invfact[x] * invfact[c-x] % MOD for x in range(c+1) ]
            
            next_dp = [ [0]*(target+1) for _ in range(ne+1) ]
            for used in range(ne+1):
                for s in range(target+1):
                    val = dp[used][s]
                    if not val:
                        continue
                    for x in range(c+1):
                        k2 = used + x
                        if k2 > ne: break
                        s2 = s + d*x
                        if s2 > target: break
                        next_dp[k2][s2] = (next_dp[k2][s2] + val * inv_contrib[x]) % MOD
            dp = next_dp
        
        ways = dp[ne][target]
        if ways == 0:
            return 0
        
        return ways * fact[ne] % MOD * fact[no] % MOD
