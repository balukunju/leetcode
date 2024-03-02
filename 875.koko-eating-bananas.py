#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Find the max number of the piles
        # Run binary search from 1 to the max 
        return self.bananasPerHour(piles, 1, max(piles), h)
    
    def bananasPerHour(self, piles, low, high, h):
        while (low <= high):
            mid = (low + high)//2
            totalHours = sum((pile - 1) // mid + 1 for pile in piles)
            if totalHours <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low
# @lc code=end

