# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, new_head = None, head
        while new_head:
            next = new_head.next
            new_head.next = prev
            prev = new_head
            new_head = next
            
        return prev
            