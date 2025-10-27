# LeetCode Problem: 38. Count and Say
# Tags: String, Simulation, Run-Length Encoding
# Solved with AI assistance

class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            next_result = ""
            i = 0
            while i < len(result):
                count = 1
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    i += 1
                    count += 1
                next_result += str(count) + result[i]
                i += 1
            result = next_result
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.countAndSay(1))  # Output: "1"
    print(sol.countAndSay(4))  # Output: "1211"
