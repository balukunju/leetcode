#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        low, high = 0, len(nums)-1
        pivotIndex = len(nums)

        while pivotIndex != (k-1):
            pivotIndex = self.partition(nums, low, high)
            if pivotIndex < k:
                low = pivotIndex + 1
            else:
                high = pivotIndex - 1
        return nums[k-1]
    
    def partition(self, nums, low, high) -> int:
        pivot = nums[low]
        i, j = low + 1, high

        while i <= j:
            if nums[i] < pivot and pivot < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            if nums[i] >= pivot:
                i += 1
            if pivot >= nums[j]:
                j -= 1
        
        nums[low], nums[j] = nums[j], nums[low]
        return j        
        
# @lc code=end

