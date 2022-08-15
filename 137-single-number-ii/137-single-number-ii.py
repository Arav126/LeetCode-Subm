class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        d = {}
        
        # building a dictionary for given problem
        
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
                
                
        vl = list(d.values())
        kl = list(d.keys())
        
        ind = vl.index(1)
        return kl[ind]
        