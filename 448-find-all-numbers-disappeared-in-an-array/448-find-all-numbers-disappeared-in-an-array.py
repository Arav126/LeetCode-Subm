class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = [i for i in range(1,len(nums)+1)]
        s = set(nums)
        # print(s)
        
        # for i in nums:
        #     # print(l)
        #     # l.pop(l.index(i))
        #     s.add(i)
            
        # t = list(s)
        # print(s)
        # for i in l:
        #     print(l)
        #     if i in s:
        #         l.pop(l.index(i))
        # return l
        
        ret = []
        for i in l:
            if i not in s:
                ret.append(i)
                
        return ret
        