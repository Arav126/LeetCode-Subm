class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        # two pointers holding indexes
#         ptrpos = 0
#         ptrneg = 0 
        
#         for i in range(0,len(nums),2):
#             ptrpos = i
#             while (1):
#                 if num[ptrpos]>0:
#                     break
#                 else:
#                     ptrpos+=1
#             # ptrpos holds the first pos
            
#             while(1):
#                 if num[ptrneg]<0:
#                     break
#                 else:
#                     ptrneg+=1
                    
#             nums[]

        # approach 1
#         ret = [0] * len(nums)
#         pos, neg = 0,1
#         for i in range(len(nums)):
#             if nums[i] > 0 :
#                 ret[pos] = nums[i]
#                 pos+=2
#             if nums[i] < 0 :
#                 ret[neg] = nums[i]
#                 neg+=2
                
#         return ret
        # approach 2
        pos = [i for i in nums if i>0]
        neg = [i for i in nums if i<0]
        
        ret = []
        
        for i in range(len(pos)):
            ret.append(pos[i])
            ret.append(neg[i])
            
        return ret