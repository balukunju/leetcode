#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 0, n

        prevTrueVersion = low
        while low <= high:
            mid = (low + high)//2
            if isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low        
# @lc code=end

