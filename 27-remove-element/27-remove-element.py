class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        n = nums.count(val)
        
        while(1):
            if val in nums:
                nums.pop(nums.index(val))
            else:
                break
                
        # for i in range(n):
        #     nums.append('_')
            
        return len(nums)
        