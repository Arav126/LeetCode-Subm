class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # building a dictionary 
        d = {}
        
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
                
        for i in list(d.keys()):
            if d[i] !=1:
                return i
        