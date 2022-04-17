# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd, even = ListNode(0), ListNode(0)
        
        oddHead, evenHead = odd, even
        
        curr = head
        
        isOdd = True
        
        while curr:
            if isOdd:
                odd.next = curr
                odd = odd.next
            
            else:
                even.next = curr
                even = even.next
            
            isOdd = not isOdd
            curr = curr.next
            
        even.next = None
        odd.next = evenHead.next
        return oddHead.next