#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#      self.val = val
#      self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummynode = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                temp = list1.next
                curr = list1
                list1 = temp
            else:
                curr.next = list2
                temp = list2.next
                curr =list2
                list2 = temp
        
        if list1 or list2:
            curr.next = list1 if list1 else list2
        return dummynode.next
        
# @lc code=end

