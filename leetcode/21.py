# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        if not list1 and not list2: # both of them are empty
            return list1
        if list1 and not list2:     # only list1 exists
            return list1
        if not list1 and list2:     # only list2 exists
            return list2
        
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
            
        node = head
        while list1 and list2:
            if list1.val <= list2.val:
                node.next, list1 = list1, list1.next
            else:
                node.next, list2 = list2, list2.next
            node = node.next
        
        while list1:
            node.next, list1 = list1, list1.next
            node = node.next
        
        while list2:
            node.next, list2 = list2, list2.next
            node = node.next
            
        return head
        