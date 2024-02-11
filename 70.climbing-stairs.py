#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return b
# @lc code=end

        for i in range(1, len(nums)):
            j = i - 1
            while (j >= 0 and nums[j+1] < nums[j]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
                j -= 1
        return nums
        