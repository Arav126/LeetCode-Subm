class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums)):
            k=0
            for j in range(0, len(nums)):
                if ((i!=j) and (nums[j] < nums[i])):
                    k+=1
            ans.append(k)
            
        return ans
        