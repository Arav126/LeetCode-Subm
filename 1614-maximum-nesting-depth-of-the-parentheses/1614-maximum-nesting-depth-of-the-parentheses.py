class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        mx = 0
        
        for i in s:
            if(i == "("):
                stack.append(1)
                
            if(i == ")"):
                j = sum(stack)
                if(j > mx):
                    mx = j
                stack.pop() # automatically pops the last element
                
        return mx
        