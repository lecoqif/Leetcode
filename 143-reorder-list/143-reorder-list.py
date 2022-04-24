# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = fast = head
        prehead = ListNode(0)
        prehead.next = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            prehead = prehead.next
            
        if fast:
            slow = slow.next
            prehead = prehead.next
        
        prehead.next = None
        
        last = Solution.reverse(slow)
        
        curr = head
        
        while curr and last:
            after = curr.next
            curr.next = last
            prevLast = last.next
            last.next = after
            curr = after
            last = prevLast
        
        return head
    
    @staticmethod
    def reverse(head: ListNode) -> ListNode:
        
        prev = None
        curr = head
        
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        
        return prev
        
        
        
        
        
        