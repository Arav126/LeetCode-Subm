# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        # we only know what is ahead of us
        # when we have no idea of what's behind, copy front and loose front
        
        temp = node.next
        node.val = temp.val
        node.next = node.next.next
        del temp
        