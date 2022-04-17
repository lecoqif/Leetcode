# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = head
        
        for i in range(n):
            fast = fast.next
        
        slow = head
        
        prev = ListNode(0)
        
        prev.next = slow
        
        curr = prev
        
        while fast:
            fast = fast.next
            slow = slow.next
            curr = curr.next
        
        curr.next = slow.next
        return prev.next