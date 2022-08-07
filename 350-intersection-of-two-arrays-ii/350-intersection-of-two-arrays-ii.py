class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []
        if(len(nums2) <= len(nums1)):
            for n in nums2:
                if n in nums1:
                    nums1.pop(nums1.index(n))
                    ans.append(n)
        elif(len(nums1) < len(nums2)):
            for n in nums1:
                if n in nums2:
                    nums2.pop(nums2.index(n))
                    ans.append(n)
                    
        return ans
        