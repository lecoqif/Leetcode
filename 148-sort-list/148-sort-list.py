# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        arr = []
        
        if not head: return head
        
        while head:
            arr.append(head)
            head = head.next
        
        arr.sort(key=lambda x:x.val)
        
        for i in range(len(arr) - 1):
            arr[i].next = arr[i + 1]
            
        arr[-1].next = None
        
        return arr[0]
            