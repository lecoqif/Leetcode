# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        lesser = lesser_head = ListNode(-1)
        
        greater = greater_head = ListNode(-1)
        
        while head:
            if head.val < x:
                lesser.next = head
                lesser = lesser.next
            
            else:
                greater.next = head
                greater = greater.next
            
            head = head.next
        
        greater.next = None
        
        lesser.next = greater_head.next
        
        return lesser_head.next
            
        
        