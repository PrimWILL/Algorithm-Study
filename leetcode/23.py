# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        heap = []
        
        for x in lists:
            while x:
                heapq.heappush(heap, x.val)
                x = x.next
                
        root = ListNode()
        temp = root
        
        while heap:
            node = ListNode(heapq.heappop(heap))
            temp.next = node
            temp = temp.next
        
        return root.next