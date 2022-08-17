class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        # dynamic dict
        
        d = {}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
                
            if 2 in list(d.values()):
                letter = (list(d.keys()))[list(d.values()).index(2)]
                return letter
        