class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
            
        # checking edge indexes
        if nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums)-1
        
        ptr1 = 1
        ptr2 = len(nums)-2
        
        while(ptr1<=ptr2):
            if(nums[ptr1-1]<nums[ptr1] and nums[ptr1]>nums[ptr1+1]):
                return ptr1
            else:
                ptr1+=1
                
            if(nums[ptr2-1]<nums[ptr2] and nums[ptr2]>nums[ptr2+1]):
                return ptr2
            else:
                ptr2-=1
        