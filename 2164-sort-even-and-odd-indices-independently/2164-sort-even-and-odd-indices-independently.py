class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        # not in-place
        
        even = [nums[i] for i in range(0,len(nums),2)]
        odd = [nums[i] for i in range(1,len(nums),2)]
        
        even.sort()
        odd.sort()
        odd.reverse()
        
        ret = []
        # 0 1 2 3
        
        for i in range(len(odd)):
            ret.append(even.pop(0))
            ret.append(odd.pop(0))
            
        if len(even) == 1:
            ret.append(even.pop(0))
            
        return ret