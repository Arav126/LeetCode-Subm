# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        
        temp = head
        while(temp):
            sz+=1
            temp = temp.next
            
        # print(sz)
        if(sz == 1 and n == 1):
            del head
            return
            
        
        k = sz-n+1
        
        if(k == 1):
            temp = head
            head = head.next
            del temp
            return head
        
        temp = head
        for i in range(1,k-1):
            temp = temp.next
            
            
        garbage = temp.next
        temp.next = temp.next.next
        del garbage
        
        
        return head