class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        c = mx = 0
        for i in nums:
            if i == 1:
                c+=1
            else:
                mx = max(c, mx)
                c = 0
                
        mx = max(c, mx)
        return mx