class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        # easy = return arr.index(max(arr))
        
        # approach -1 => linear time
        
        # for i in range(1,len(arr)):
        #     if arr[i]>= arr[i-1]:
        #         continue
        #     else:
        #         return i-1 # at that point where curr is less than prev, return prev, cuz that is the peak
        
        # approach - 2 => binary test case
        
        lo = 0
        hi = len(arr)-1
        
        while(lo<hi): # needs to break at the equal to to case otherwise it's an infine loop for hi == low == peak
            m = (lo+hi)//2
                # now we can say for sure that the current value is not the peak
                # if arr[m]>=arr[m-1] : this is true for the peak as well, and will avoid the peak and go ahead
                # we need something that confirms that the current is not the peak, so we can avoid it and go ahead
            if arr[m] < arr[m+1]: # arr of the mid value is greater than prev move forward
                lo = m+1
            else:
                hi = m # shift hi to that point, since we know there's nothing ahead of it there
                
        return lo
                