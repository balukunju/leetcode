#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if not lists or n == 0:
            return None
        
        for i in range(1, n):
            l1, l2 = lists[0], lists[i]
            lists[0] = self.merge(l1, l2)
        return lists[0]
        
    def merge(self, list1, list2):
        dummy = ListNode()
        temp = dummy

        while (list1 and list2):
            if list1.val < list2.val:
                temp.next, list1 = list1, list1.next
            else:
                temp.next, list2 = list2, list2.next
            temp = temp.next

        temp.next = list1 if list1 else list2
        return dummy.next        
# @lc code=end

