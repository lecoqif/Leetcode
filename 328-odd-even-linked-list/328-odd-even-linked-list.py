# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        curr = head
        
        even, odd = ListNode(-1), ListNode(-1)
        
        preHead, preEven = odd, even
        
        i = 1
        
        while head:
            if i % 2 == 1:
                odd.next = head
                odd = odd.next
            
            else:
                even.next = head
                even = even.next
                
            i += 1
            head = head.next
        
        even.next = None
        odd.next = preEven.next
        
        return preHead.next
        
        
                
        
        
        
        
        
        
        