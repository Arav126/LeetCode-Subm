class Solution:
    def countAsterisks(self, s: str) -> int:
        
        switch = 1
        ret = 0
        for i in s:
            if i == "*" and switch ==1:
                ret+=1
            if i =="|" and switch ==1:
                switch = 0
            elif i =="|" and switch ==0:
                switch =1
                
        return ret

                    
        