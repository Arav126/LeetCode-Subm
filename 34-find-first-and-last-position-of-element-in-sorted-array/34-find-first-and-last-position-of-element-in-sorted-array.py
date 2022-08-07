class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
#         ans = []
#         f = 0
#         for i in range(0, len(nums)):
#             if(nums[i] == target):
#                 ans.append(i)
#                 f=1
#                 break
                
#         for j in range(len(nums)-1, -1, -1):
#             if(nums[j] == target):
#                 ans.append(j)
#                 break
                
#         if f == 0 :
#             ans.append(-1)
#             ans.append(-1)            
                
#         return ans

        ans =[]
        if (target not in nums):
            return [-1,-1]
        
        ans.append(nums.index(target))
        nums.sort(reverse = True)
        ans.append(len(nums)-nums.index(target)-1)
        
        return ans