class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []
        
        for i in nums1:
            if i in nums2:
                ind = nums2.index(i)
                split = nums2[ind+1 : ]
                
                mx = i
                flag = 0
                for j in split:
                    if (j > mx):
                        flag = 1
                        ans.append(j)
                        break
                    
                if flag == 0:
                    ans.append(-1)
            else:
                ans.append(-1)
                
            
        return ans
        