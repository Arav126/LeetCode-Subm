class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        while(len(nums)!=0):
            mx = max(nums)
            nums.pop(nums.index(mx))
            
            if mx not in nums:
                return mx
            else:
                for i in range(0, nums.count(mx)):
                    nums.pop(nums.index(mx))
                    
            
        return -1
            
        