class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        ret=0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] == nums[j] and i<j:
                    ret+=1
                    
        return ret
        