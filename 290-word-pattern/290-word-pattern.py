class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        lc = s.split()
        d = {}   
        
        if len(lc)!=len(pattern):
            return False
        
        for i in range(len(pattern)):
            p = pattern[i]
            if p not in d:
                d[p] = lc[i]
            elif p in d: #meaning in d
                if d[p] != lc[i]:
                    return False
              
        # values must also be unique
        chk = list(d.values())
        if len(chk) != len(set(chk)):
            return False
        return True
        