class Solution:
    def romanToInt(self, s: str) -> int:
        
        d = {
            "I":1,
            "V":5, 
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
        }
        
        ans = []
        sum = 0
        i = 0
        while(i!=len(s)):
            
            if(i != len(s)-1):
                temp = s[i] + s[i+1]
                
                if temp in list(d.keys()):
                    sum+=d[temp]
                    ans.append(sum)
                    i+=2
                    continue
                
               
                
            ind = s[i]
            sum+=d[ind]
            ans.append(sum)
            i+=1
            
        print(ans)
        return sum
        