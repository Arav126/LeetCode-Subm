class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        # ans = [0] * (len(nums)-1)
        ans = [] * (len(nums)-1)
        
        for i in range(0,len(nums)):
            ans.insert(index[i],nums[i])
            
        return ans