# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if(head == None)or(head.next == None):
            return head
        
        # using single pointer
        cur = head
        
        while(cur.next):
            
            if cur.next.val == cur.val:
                temp = cur.next
                cur.next = cur.next.next
                del temp
            else:
                cur = cur.next
                
        return head
        