# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        f = []
        # d = {}
        
        if(root == None):
            return []
        
        queue = []
        queue.append(root)
        queue.append(None)
        
        while(len(queue)>0):
            j = queue.pop(0)
            if j!=None:
                f.append(j.val)
            else:
                f.append(None)
                
            if j is not None: 
                if j.left is not None:
                    queue.append(j.left)

                if j.right is not None:
                    queue.append(j.right)
            elif(len(queue)>0):
                queue.append(None)
            
        ret = []
        temp = []
        for i in f:
            if i is not None:
                temp.append(i)
            else:
                ret.append(temp)
                temp = []
                
        # print(ret)
            
                
        return ret
    
        