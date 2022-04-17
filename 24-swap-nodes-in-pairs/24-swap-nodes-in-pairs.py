# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        afterHead = head.next.next
        
        nextNode = head.next
        
        nextNode.next = head
        
        head.next = self.swapPairs(afterHead)
        
        return nextNode