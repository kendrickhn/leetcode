class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        # convert string to list for in-place edits
        res = list(dominoes)
        
        prev = -1            # index of the last non-'.' we processed
        prev_char = 'L'      # assume a virtual 'L' at -1
        
        # scan through dominoes, plus one extra position as a virtual 'R' at n
        for i in range(n + 1):
            # determine current force character
            curr_char = dominoes[i] if i < n else 'R'
            if i < n and curr_char == '.':
                continue
            
            # now we have a segment between prev and i, bounded by prev_char and curr_char
            if prev_char == curr_char:
                # e.g. "L ... L" or "R ... R": fill entire segment with that same force
                for k in range(prev + 1, i):
                    res[k] = curr_char
            elif prev_char == 'R' and curr_char == 'L':
                # "R ... L": fill inward from both ends
                left, right = prev + 1, i - 1
                while left < right:
                    res[left]  = 'R'
                    res[right] = 'L'
                    left  += 1
                    right -= 1
                # if left == right, it stays '.' (balanced)
            # else prev_char=='L' and curr_char=='R': "L ... R" => leave as '.'
            
            # move to next segment
            prev = i
            prev_char = curr_char
        
        # join back to string
        return ''.join(res)


# Example usage:
if __name__ == '__main__':
    sol = Solution()
    print(sol.pushDominoes("RR.L"))           # RR.L
    print(sol.pushDominoes(".L.R...LR..L..")) # LL.RR.LLRRLL..
