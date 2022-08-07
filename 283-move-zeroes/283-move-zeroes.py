class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         k = 0
#         while (0 in nums):
#             nums.remove(0)
#             k+=1
        
#         for i in range(0, k):
#             nums.append(0)
        
        
#         i = 0
        
#         while(i != len(nums)):
#             if(nums[i] == 0):
#                 nums.pop(i)
#                 nums.append(0)
                
#             # else:
#                 # i+=1
#             i+=1
                
            # if(i == len(nums)):
            #     break
#         k = 0
#         while(1):
#             if(nums[i] == 0):
#                 k+=1
#                 nums.pop(i)
                
#             if(i == len(nums)-2):
#                 break
                
#         for j in range(0, k+1):
#             nums.append(0)
            
#         ans = []
#         j = 0         
#         for i in nums:
#             if (i == 0):
#                 j+=1
#                 # nums.pop(nums.index(0))
#             else:
#                 ans.append(i)
                
#         ans.extend([0] * j)
#         return ans
        j=0
        while(1):
            if 0 in nums:
                j+=1
                nums.pop(nums.index(0))
            else:
                break
            
                
        nums.extend([0] *j)
        return nums
            