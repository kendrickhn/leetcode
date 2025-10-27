# solved in 10:00
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = nums.count(0)
        if count > 0:
            while count != 0:
                nums.remove(0)
                nums.append(0)
                count -= 1