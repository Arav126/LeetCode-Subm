class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        
        d = {}
        
        for i in range(len(messages)):
            wc = messages[i].split() #default
            wc = len(wc)
            if senders[i] not in d:
                d[senders[i]] = wc
            else:
                d[senders[i]]+=wc
                
        # print(d)
                
        mx = max(list(d.values()))
        
        ret = []
        while(1):
            if mx in (list(d.values())):
                val = (list(d.keys()))[list(d.values()).index(mx)]
                ret.append(val)
                
                d.pop(val)
            else:
                break
                
        # print(ret)
        
        ret.sort()
        return ret[-1]
        
        