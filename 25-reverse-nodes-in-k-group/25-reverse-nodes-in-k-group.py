# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def length(self, head: ListNode) -> int:
        curr = head
        size = 0
        
        while curr:
            curr = curr.next
            size += 1
        
        return size
    
    def kthNode(self, head: ListNode, k: int) -> ListNode:
        curr = head
        idx = 1
        
        while curr:
            curr = curr.next
            idx += 1
            
            if idx == k:
                return curr
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or self.length(head) < k or k <= 1: 
            return head
        
        lastInGroup = self.kthNode(head, k)
        
        after = self.reverseKGroup(lastInGroup.next, k)
        
        lastInGroup.next = None
        
        prev, curr = None, head
        
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        head.next = after
        
        return prev
        
        
        
        
        
        