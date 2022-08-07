class Solution:
    
    def swapp(self, sin1: str, sin2: str, i: int, j: int):
        temp = ''
        temp+= sin1[i]
        
        l1 = list(sin1)
        l2 = list(sin2)
        
        l1[i] = l2[j]
        l2[j] = temp
        
        sin1 = ''.join(l1)
        sin2 = ''.join(l2)
        
        return sin1, sin2
    
    
    
    
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        if(len(s1) !=  len(s2)):
            return False
        
        if(s1 == s2):
            return True
        
        t1 = s1
        t2 = s2
        
        for i in range(0, len(s1)):
            for j in range(0, len(s1)):
                t1 = s1 #only now it hits properly
                t2 = s2
                
                # t1,t2 = self.swapp(t1,t2,i,j)
                
                t2 = self.swapNew(t2, i, j)
                
                # print(t1, ' | ', t2, end='\n')
                if t1 == t2 :
                    return True
                
        return False
    
    def swapNew(self, t2: str, i: int, j:int):
        temp = ''
        
        l2 = list(t2)
        
        temp += l2[i]
        l2[i] = l2[j]
        l2[j] = temp
        
        t2 = ''.join(l2)
        
        return t2
        
        
        
            
            
            
            
            

        
        
        