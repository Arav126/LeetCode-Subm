class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        upper = len(nums)-1
        
        while(low<=upper):
            mid = (low+upper)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid+1
            elif target < nums[mid]:
                upper = mid-1
                
        return -1
        
        
            