# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         temp = head.next
#         dummy = ListNode(-1)
#         dummy.next = head
        
#         while(temp):
#             d = temp
#             d.next = dummy.next
#             dummy.next = d
#             print(dummy.val)
            
#             temp = temp.next
        
#         return dummy.next

        # prev = head
        # cur = head.next
        # n = head.next.next
            # => caused a cycle
            
        if(head == None)or(head.next == None):
            return head
        
        prev = None
        cur = head
        n = head.next
        
        while(cur):
            n = cur.next # holding next value to cur
            cur.next = prev
            prev = cur
            cur = n
            
        head = prev
        
        return head
            
            
            
        
        