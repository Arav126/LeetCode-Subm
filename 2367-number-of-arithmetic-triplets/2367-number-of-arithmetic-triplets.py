class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        c=0
        for k in range(0, len(nums)):
            for j in range(0, k):
                for i in range(0, j):
                    if(nums[j] - nums[i] == diff)and(nums[k] - nums[j] == diff):
                        c+=1
        
        return c