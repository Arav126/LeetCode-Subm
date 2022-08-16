class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        
        distList = [(0-abs(i)) for i in nums]
        # nums will also have the same index associated with distList
        mx = max(distList)
        # cd = distList.count(mx)
        # val = nums[distList.index(mx)]
        
        
        retIndex = []
        for i in range(len(distList)):
            if distList[i] == mx:
                retIndex.append(i)
                
        dummy = [nums[i] for i in retIndex]
        
        return max(dummy)
            
        
    
            
        
        
        
        