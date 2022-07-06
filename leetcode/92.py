# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cnt = 1
        root = head
        left_end = None
        
        new_end = None
        temp = new_end
        while root:
            if left <= cnt <= right:
                node, root = root, root.next
                node.next = temp
                temp = node
                if cnt == left:
                    new_end = node
                if cnt == right:
                    new_end.next = root
                    if left_end:
                        left_end.next = temp
                    else:
                        head = temp
                    break 
            else:    
                left_end, root = root, root.next
            cnt += 1
        return head