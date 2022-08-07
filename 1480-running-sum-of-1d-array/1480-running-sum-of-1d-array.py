class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        ans.append(nums[0])
        for i in range(1, len(nums)):
            j = ans[i-1] + nums[i]
            ans.append(j)
            
        return ans