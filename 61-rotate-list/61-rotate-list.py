# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        curr, last = head, None
        
        listLength = 0
        
        while curr:
            listLength += 1
            
            if not curr.next:
                last = curr
            
            curr = curr.next
            
        k = k % listLength
        
        if k == 0: return head
        
        detachNodeIndex = listLength - k
        
        i = 1
        
        curr = head
        
        newHead = None
        
        while curr:
            if i == detachNodeIndex:
                newHead = curr.next
                curr.next = None
                break
            
            curr = curr.next
            
            i += 1
        
        last.next = head
        
        return newHead
            
                