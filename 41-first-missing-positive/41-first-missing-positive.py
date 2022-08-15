class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        f = [i for i in nums if i>=0]
        
        if len(f) == 0:
            return 1
        
#         i=0
#         mn = min(f)
        
#         while(1):
#             if nums[i] 

#         f.sort()
#         j = 0
#         for i in range(f[0], f[-1]+1):
#             if i == f[j]:
#                 j+=1
#             else:
#                 return i
            
#         return i+1

        s = set(f)
        f = list(s)
        f.sort()
    
        if f[0] > 1:
            return 1
        
        if f[0] == 0:
            mn = 0
        elif f[0] == 1:
            mn = 1
            
        j = 0
        for i in range(mn,f[-1]+1): # if its 0 start from 0, 1 then start from 1
            if f[j] == i:
                j+=1
            else:
                return i
            
        return i+1
        