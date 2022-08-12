class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        # print(l)
        
        for i in range(0, len(l)):
            temp = l[i]
            temp = temp[::-1]
            l[i] = temp
            
        ret = ' '.join(l)
        return ret
            
        