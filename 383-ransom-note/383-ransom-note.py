class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        l = [i for i in ransomNote]
        dynamic = ''.join(l)
        # print(dynamic)
        
        for i in magazine:
            if i in l:
                j = l.pop(l.index(i))
                print(j)
                
        if len(l) == 0:
            return True
        else:
            return False
        