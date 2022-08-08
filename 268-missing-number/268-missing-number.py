class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        l = [i for i in range(0, len(nums)+1)]
        # print(l)
        ans = []
        for i in nums:
            if i in l:
                l.pop(l.index(i))
                # print(l)
            else:
                ans.append(i)
                # print("h", ans)
                
        # print(ans)
        
        return l[0]
        