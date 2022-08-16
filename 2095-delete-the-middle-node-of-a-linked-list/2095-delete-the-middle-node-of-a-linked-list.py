# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head.next == None:
            head = None
            return head
        
        temp = head
        n=0
        while temp:
            n+=1
            temp = temp.next
            
        if(n%2 == 1):
            k = ceil(n/2)
        else:
            k = (n/2)+1
            
        temp = head
        for i in range(1, int(k)-1):
            temp = temp.next
            
        garbage = temp.next
        temp.next = temp.next.next
        del garbage
        
        return head 