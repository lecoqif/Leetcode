# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        
        
        curr = head
        
        def find_length(node):
            ret = 0
            while node is not None:
                ret += 1
                node = node.next
            
            return ret
                
        length = find_length(curr)
        
        
        k = k % length
        
        if k == 0 or length == 1:
            return head
        
        def find_node(index, node):
            curr = 0
            while True:
                curr += 1
                if curr == index:
                    return node
                
                node = node.next
            
            
        curr = head
        break_node = find_node(length - k, curr)
        curr = head
        last_node = find_node(length, curr)
        new_head = break_node.next
        break_node.next = None
        last_node.next = head
        return new_head
        