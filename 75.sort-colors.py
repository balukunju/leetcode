#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = {}
        for i in range(0, len(nums)):
            if nums[i] in counts:
                counts[nums[i]] += 1
            else:
                counts[nums[i]] = 1
        sorted_counts = dict(sorted(counts.items()))
        n = 0
        for key, value in sorted_counts.items():
            for i in range(value):
                nums[n] = key
                n += 1         
# @lc code=end

