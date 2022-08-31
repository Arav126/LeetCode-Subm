class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        fh = len(s)//2
        fv = 0
        
        for i in range(fh):
            if s[i] in vow:
                fv+=1
                
        lv = 0
        for i in range(fh,len(s)):
            if s[i] in vow:
                lv+=1
                
        if fv == lv:
            return True
        else:
            return False