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

#         ans =[]
#         if (target not in nums):
#             return [-1,-1]
        
#         ans.append(nums.index(target))
#         nums.sort(reverse = True)
#         ans.append(len(nums)-nums.index(target)-1)
        
#         return ans

        # implementation using binary search
    
        lo = 0
        hi = len(nums)-1
        
        ind = -1
        while(lo<=hi):
            mi = (lo+hi)//2
            if nums[mi] == target:
                ind = mi
                break
            elif nums[mi]> target:
                hi = mi-1
            else:
                lo = mi+1
                
        # print(ind) # this index is not the first or last occurence, but we have a position now
        
        if ind == -1:
            return [-1,-1]
        
        f = l = ind
        while(1):
            if f-1 > -1 and nums[f-1] == nums[f]:
                f-=1
            elif l+1 < len(nums) and nums[l+1] == nums[l]:
                l+=1
            else:
                break
                
        return [f,l]