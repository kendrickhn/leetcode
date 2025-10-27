class Solution:
    def triangleType(self, nums):
        # Sort sides so nums[0] <= nums[1] <= nums[2]
        nums.sort()
        a, b, c = nums
        
        # Check triangle inequality
        if a + b <= c:
            return "none"
        
        # All three equal ⇒ equilateral
        if a == c:
            return "equilateral"
        # Exactly two equal ⇒ isosceles
        if a == b or b == c:
            return "isosceles"
        # All different ⇒ scalene
        return "scalene"
