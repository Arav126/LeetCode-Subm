class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        mx = fmx = max(nums)
        i = 1
        while(1):
            if(len(nums)==0):
                return fmx
            if mx in nums:
                nums.pop(nums.index(mx))
            else:
                i+=1
                mx = max(nums)
                if i == 3:
                    return mx