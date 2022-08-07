class Solution:
    def isValid(self, s: str) -> bool:
        s1,s2,s3 = [], [], []
        vs = []
        
        for i in s:
            if(i == "("):
                s1.append(1)
            if(i == ")"):
                if(sum(s1) == 0):
                    return False
                s1.pop()
                
            if(i == "["):
                s2.append(1)
            if(i == "]"):
                if(sum(s2) == 0):
                    return False
                s2.pop()
                
            if(i == "{"):
                s3.append(1)
            if(i == "}"):
                if(sum(s3) == 0):
                    return False
                s3.pop()
                
                
            if(i == "("):
                vs.append(1)
            elif(i == "["):
                vs.append(2)
            elif(i == "{"):
                vs.append(3)
                
            if(i == ")"):
                if(vs[-1] == 2 or vs[-1] == 3):
                    return False
                else:
                    vs.pop()
            elif(i == "]"):
                if(vs[-1] == 1 or vs[-1] == 3):
                    return False
                else:
                    vs.pop()
            elif(i == "}"):
                if(vs[-1] == 1 or vs[-1] == 2):
                    return False
                else:
                    vs.pop()
            
            
                
        if(sum(s1) == 0 and sum(s2) == 0 and sum(s3) == 0):
            return True
        else:
            return False
                
            
                
        