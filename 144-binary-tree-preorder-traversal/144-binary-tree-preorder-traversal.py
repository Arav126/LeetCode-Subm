# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ret = []
        
        preorder(root, ret)
        
        # print(ret)
        return ret
        
def preorder(root, ret):
    if (root):
        ret.append(root.val)
        preorder(root.left, ret)
        preorder(root.right, ret)
        
        