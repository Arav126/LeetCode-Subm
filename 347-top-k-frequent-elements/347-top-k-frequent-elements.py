class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
                
        sv = list(d.values())
        sv.sort()
        sv.reverse()
        
        ret = []
        for i in range(k):
            val = list(d.keys())[list(d.values()).index(sv[i])] 
            d.pop(val)
            ret.append(val)
        
        return ret