class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Base cases
        full    = [0] * (n+1)
        partial = [0] * (n+1)
        full[0], full[1] = 1, 1
        partial[0], partial[1] = 0, 0
        
        for i in range(2, n+1):
            # Recurrence
            full[i] = (
                full[i-1]                    # 1 vertical domino
                + full[i-2]                  # 2 horizontal domino
                + 2 * partial[i-1]          # 2 cách dùng tromino trên partial
            ) % MOD
            
            partial[i] = (
                partial[i-1]                # nối thêm vertical domino vẫn còn lõm
                + full[i-2]                 # tạo lõm bằng 1 tromino
            ) % MOD
        
        return full[n]
