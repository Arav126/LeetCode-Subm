class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for i in range(0, len(nums)):
            if(nums[i] == target):
                return i
            if(target<nums[i]):
                return i
            
            
        if(target > nums[-1]):
            return (len(nums))
            
                