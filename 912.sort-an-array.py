#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(A):
            LA = len(A)
            if (LA == 1):
                return A
            LHA, RHA = mergeSort(A[:LA//2]), mergeSort(A[LA//2:])
            return merge(LHA, RHA)
        
        def merge(LH, RH):
            LLH, LRH = len(LH), len(RH)
            S, i, j = [], 0, 0
            while (i < LLH and j < LRH):
                if LH[i] <= RH[j]:
                    i, _ = i+1, S.append(LH[i])
                else:
                    j, _ = j+1, S.append(RH[j])
            return S + (RH[j:] if i == LLH else LH[i:])
        
        return mergeSort(nums)        
        
#Reference : https://leetcode.com/problems/sort-an-array/solutions/461394/python-3-eight-sorting-algorithms-with-explanation
    
# @lc code=end

