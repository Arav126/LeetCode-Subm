class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = 0
        carry = 0
        
        i = 0
        while(i < len(nums)):
            if nums[i] in nums[i+1:]:
                val = nums[i]
                for j in range(2):
                    nums.pop(nums.index(val))
                pairs+=1
            else:
                i+=1
                
        carry = len(nums)
        
        ret = []
        ret.append(pairs)
        ret.append(carry)
        
        return ret
            
        