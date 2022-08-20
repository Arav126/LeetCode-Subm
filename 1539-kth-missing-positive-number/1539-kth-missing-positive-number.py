class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        shit = [i for i in range(1,arr[-1]+1)]
        
        for i in arr:
            if i in shit:
                shit.pop(shit.index(i))
                
        if k>len(shit):
            return (arr[-1] + (k-len(shit)))
            
            # pass
        else:
            return shit[k-1]
        