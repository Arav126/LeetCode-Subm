import bisect

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        # complexity n^2
        s = []
        
        for i in range(len(nums)):
            for j in range(0,i):
                s.append(nums[i]+nums[j])
                
        s.sort()
        ind = bisect.bisect_left(s,k)
        
        if ind == 0:
            return -1
        return s[ind-1]
        