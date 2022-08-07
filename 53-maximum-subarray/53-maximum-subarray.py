class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currSum = nums[0]
        maxSum = []
        maxSum.append(nums[0])
        for i in nums[1:]:
            currSum = max(i, currSum + i)
            maxSum.append(currSum)
            
        print(maxSum)
            
        return max(maxSum)
        