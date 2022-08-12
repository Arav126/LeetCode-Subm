class Solution:
    def reverseWords(self, s: str) -> str:
        
        l = s.split(' ')
        l = [i for i in l if i!='']
        print(l)
        l.reverse()
        ret = ' '.join(l)
        return ret
        