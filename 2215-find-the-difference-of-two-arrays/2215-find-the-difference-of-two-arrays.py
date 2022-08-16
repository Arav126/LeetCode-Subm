class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        l0 = [i for i in nums1 if i not in nums2]
        l1 = [i for i in nums2 if i not in nums1]
        
        return [list(set(l0)), list(set(l1))]
        
        