class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        # easy = return arr.index(max(arr))
        
        # approach -1 => linear time
        
        for i in range(1,len(arr)):
            if arr[i]>= arr[i-1]:
                continue
            else:
                return i-1 # at that point where curr is less than prev, return prev, cuz that is the peak