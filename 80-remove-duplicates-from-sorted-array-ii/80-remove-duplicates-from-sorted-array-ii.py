class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i=0
        while(i < len(nums)):
            count = nums.count(nums[i])
            if count<=2:
                i+=1
            else:
                it = nums.count(nums[i]) - 2
                
                for j in range(it):
                    nums.pop(i)
            
        return len(nums)
        