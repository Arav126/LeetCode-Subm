class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        ans =[]
        
        for i in range(0, len(nums)):
            j = nums[i]*nums[i]
            ans.append(j)
            
        ans.sort()
        
        return ans
            
            
        