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
        
        stack = []
        
        prehead = ListNode(0)
        prehead.next = head
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            prehead = prehead.next
            slow = slow.next
            
        # Odd length linked list
        if fast:
            prehead = prehead.next
            slow = slow.next
        
        prehead.next = None
        
        while slow:
            stack.append(slow)
            slow = slow.next
        
        curr = head
        
        while curr and stack:
            after = curr.next
            last = stack.pop()
            curr.next = last
            last.next = after
            curr = after
            
        return head
        
        
        
        
        