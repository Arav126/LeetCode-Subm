# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # two pointers
        p1,p2 = headA, headB
        s = set()
        
        while(p1!=None and p2!=None):
            if p1 not in s:
                s.add(p1)
            else:
                return p1
            
            if p2 not in s:
                s.add(p2)
            else:
                return p2
            
            p1 = p1.next
            p2 = p2.next
            
        while(p1):
            if p1 not in s:
                s.add(p1)
            else:
                return p1
            
            p1=p1.next
            
        while(p2):
            if p2 not in s:
                s.add(p2)
            else:
                return p2
            p2 = p2.next
            
        return None
            
        
        