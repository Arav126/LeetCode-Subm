class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        # Linear Search 
        
#         for i in letters:
#             if i > target:
#                 return i
            
#         return letters[0] # if nothing is greater
            
        # binary search
        
        lo = 0 
        hi = len(letters)-1
        
        while(lo<=hi):
            m = (lo+hi)//2
            if letters[m] > target:
                hi = m-1
            elif letters[m] <= target:
                lo = m+1
                
        if hi+1 == len(letters):
            return letters[0]
        else:
            return letters[hi+1] # same as bisect left