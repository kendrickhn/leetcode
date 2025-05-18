class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        
        # 1) Generate all valid column colorings (no two vertically adjacent equal)
        # Represent a column as an integer in base-3 of length m
        valid = []
        def is_valid(col):
            # Check no two adjacent cells in column are equal
            prev = -1
            for _ in range(m):
                c = col % 3
                if c == prev:
                    return False
                prev = c
                col //= 3
            return True
        
        for col in range(3**m):
            if is_valid(col):
                valid.append(col)
        
        # 2) Precompute compatibility: can place col2 to the right of col1?
        # They must differ at each row: in base-3 digits
        comp = {c: [] for c in valid}
        for c1 in valid:
            for c2 in valid:
                x, y = c1, c2
                ok = True
                for _ in range(m):
                    if (x % 3) == (y % 3):
                        ok = False
                        break
                    x //= 3
                    y //= 3
                if ok:
                    comp[c1].append(c2)
        
        # 3) DP over columns
        # dp[col_index][state] = ways; we only keep one array prev_dp for previous column
        prev_dp = {c: 1 for c in valid}  # for first column, each valid coloring counts 1
        
        for _ in range(n-1):
            new_dp = {c: 0 for c in valid}
            for c1, ways in prev_dp.items():
                if ways:
                    for c2 in comp[c1]:
                        new_dp[c2] = (new_dp[c2] + ways) % MOD
            prev_dp = new_dp
        
        # 4) Total ways = sum over dp at last column
        return sum(prev_dp.values()) % MOD
