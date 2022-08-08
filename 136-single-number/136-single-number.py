class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        d = {}
        
        for i in range(0, len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]]+=1
                
        print(d)
        
        for i in list(d.keys()):
            if d[i] == 1:
                return i
        