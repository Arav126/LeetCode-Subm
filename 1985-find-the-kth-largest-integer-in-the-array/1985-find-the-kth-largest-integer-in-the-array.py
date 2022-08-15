class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        f = [int(i) for i in nums]
        
        f.sort()
        
        return str(f[len(f) - k])
        