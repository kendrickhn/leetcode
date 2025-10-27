# LeetCode 1922 - Count Good Numbers
# Solved with AI help on 2025-04-13

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        def mod_pow(a, b):
            result = 1
            a %= MOD
            while b > 0:
                if b % 2 == 1:
                    result = (result * a) % MOD
                a = (a * a) % MOD
                b //= 2
            return result
        
        even_count = (n + 1) // 2
        odd_count = n // 2
        return (mod_pow(5, even_count) * mod_pow(4, odd_count)) % MOD
