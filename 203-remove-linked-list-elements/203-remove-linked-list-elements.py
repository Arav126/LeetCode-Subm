# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        temp = head
        
        if(head == None):
            return head
        
        while(1):
            if head!=None and head.val == val :
                garbage = head
                head = head.next
                del garbage
            else :
                break
                
        if(head == None) or head.next == None:
            return head
                
        
        while(temp.next != None):
            while(1):
                if temp.next.val == val:
                    garbage = temp.next
                    temp.next = temp.next.next # in case of last element, it ll just point to None
                    del garbage
                else :
                    break
                
                if temp.next == None:
                    break
            if(temp.next == None):
                break
            temp = temp.next
            
        return head
                
        