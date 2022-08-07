# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        postorder(root, ret)
        
        return ret
    
def postorder(root, ret):
    if(root):
        postorder(root.left, ret)
        postorder(root.right, ret)
        ret.append(root.val)