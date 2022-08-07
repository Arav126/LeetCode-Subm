class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
            
        nums1.sort()
        
        if len(nums1)%2 == 1 :
            return (nums1[int((len(nums1)-1)/2)])
        elif len(nums1) == 1 : 
            return nums1[0]
        else :
            a = nums1[int((len(nums1)/2)-1)]
            b = nums1[int(len(nums1)/2)]
            s = []
            s.append(a)
            s.append(b)
            return sum(s)/2