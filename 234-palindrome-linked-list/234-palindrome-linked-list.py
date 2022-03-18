# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ret = []
        
        node = head
        
        while node:
            ret.append(node.val)
            node = node.next
        
        for i in range(len(ret) // 2):
            if ret[i] != ret[len(ret) - 1 - i]:
                return False
        
        return True