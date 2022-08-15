class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # building a dictionary
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
                
        ret = []
        for i in list(d.keys()):
            if d[i] > len(nums)/3:
                ret.append(i)
        
        return ret