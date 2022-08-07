class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        g = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if(i<j)and(abs(nums[i]-nums[j]) == k):
                    g+=1
                    
        return g