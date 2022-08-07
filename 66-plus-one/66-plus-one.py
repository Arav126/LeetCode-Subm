class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(i) for i in digits]
        s = ''.join(digits)
        i = int(s)
        i+=1
        
        s = str(i)
        ret = [i for i in s]
        return ret
        