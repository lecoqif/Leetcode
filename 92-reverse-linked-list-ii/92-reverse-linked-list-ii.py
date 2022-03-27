# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        startNode, endNode, prev, after = None, None, None, None
        
        prehead = ListNode(-1)
        
        prehead.next = head
        
        curr = prehead
        
        i = 0
        
        while curr:
            if i + 1 == m:
                prev = curr
                startNode = curr.next
            
            if i + 1 == n:
                after = curr.next.next
                endNode = curr.next
                break
            
            curr = curr.next
            i += 1
        
        endNode.next = None
        
        root, tail = self.reverseList(startNode)
        
        prev.next = root
        
        tail.next = after
        
        return prehead.next
        
    
    def reverseList(self, head) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        
        return prev, head
        
        
        