class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        # for i in range(len(words)):
        #     temp = words[i]
        #     words[i] = temp.lower()
            
        
        ret = []
        
        for i in words:
            t1,t2,t3=0,0,0
            
            for j in i:
                if j.lower() not in "qwertyuiop":
                    t1 = 0
                    break
                t1 = 1
                
            for j in i:
                if j.lower() not in "asdfghjkl":
                    t2 = 0
                    break
                t2 = 1
                
            for j in i:
                if j.lower() not in "zxcvbnm":
                    t3 = 0
                    break
                t3 = 1
                
            if t1 or t2 or t3:
                ret.append(i)
                
        return ret
                    
        