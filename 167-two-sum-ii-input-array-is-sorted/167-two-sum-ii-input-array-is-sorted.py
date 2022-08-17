class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
#         ans = []
#         for i in range(0, len(numbers)):
#             for j in range(i+1, len(numbers)):
#                 k = numbers[i] + numbers[j]
#                 if(k == target):
#                     ans.append(i+1)
#                     ans.append(j+1)
#                     break
                    
                
#         return ans

    # building a dictionary
        d = {}

        for i in range(len(numbers)):
            d[numbers[i]] = i

        for i in range(len(numbers)):
            comp = target - numbers[i]
            if (comp in d) and (d[comp]!=i): #if the required differnce exists and it is not the same element itself
                return [i+1, d[comp]+1]