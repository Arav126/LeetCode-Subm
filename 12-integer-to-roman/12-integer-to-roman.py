import bisect

class Solution:
    def intToRoman(self, num: int) -> str:
        
        d = {
            1:"I",
            4:"IV",
            5:"V", 
            9:"IX",
            10:"X",
            40:"XL",
            50:"L",
            90:"XC",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M",  
        }
        
        ans = []
        ret = ''
        # print(list(d.keys()))
        while(num != 0):
            if num in list(d.keys()):
                
                ret += d[num]
                num-=num
                ans.append(num)
                continue
                
            pos = bisect.bisect_left(list(d.keys()), num)
            val = list(d.keys())[pos-1]
            num-=val
            ret += d[val]
            ans.append(val)
            
        print(ans)
        return ret
            