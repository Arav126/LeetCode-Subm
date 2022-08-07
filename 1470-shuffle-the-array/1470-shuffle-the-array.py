class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1,l2,ans = [], [], []
        
        for i in range(0, n):
            l1.append(nums[i])
            
        for i in range(n, len(nums)):
            l2.append(nums[i])
            
        for i in range(0, len(l1)):
            ans.append(l1[i])
            ans.append(l2[i])
            
        return ans
        