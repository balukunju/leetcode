#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1
        if len(nums) == 0 and nums[0] == target:
            return 0
        while L <= R:
            mid = (L+R)//2
            if target < nums[mid]:
                R = mid - 1
            elif target > nums[mid]:
                L = mid + 1
            else:
                return mid
        return -1        
# @lc code=end

