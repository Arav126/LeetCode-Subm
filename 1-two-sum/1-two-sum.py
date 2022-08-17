class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0,len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if(nums[i] + nums[j] == target):
        #             return [i,j]
        
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
            
        for i in range(len(nums)):
            comp = target - nums[i]
            if (comp in d) and d[comp]!=i:
                return [i,d[comp]]