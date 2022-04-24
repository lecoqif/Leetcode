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
        
        if not head: return
        
        def reorder(root: ListNode, curr: ListNode) -> ListNode:
            if not curr: return root
            
            root = reorder(root, curr.next)
            
            if not root: return None
            
            if root == curr or root.next == curr:
                curr.next = None
            
            else: 
                root.next, curr.next = curr, root.next
            
            return curr.next
                
        
        reorder(head, head.next)
        
    
        
        
        
        
        
        