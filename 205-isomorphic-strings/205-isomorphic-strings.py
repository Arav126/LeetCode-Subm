class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        d1,d2 = {},{}
        
        # for i in range(len(s)):
        #     print(d1,d2)
        #     if s[i] not in d1 and t[i] not in d2:
        #         d1[s[i]] = t[i]
        #         d2[t[i]] = s[i]
        #     elif s[i] in d1:
        #         if d1[s[i]] == t[i] and d2[t[i]] == s[i]:
        #             continue
        #         else:
        #             return False
        # return True
        
        for i in range(len(s)):
            # print(d1)
            if s[i] not in d1 and t[i] not in list(d1.values()): # unique check as well
                d1[s[i]] = t[i]
            else:
                # check
                if s[i] not in d1: # rough code check, could have done it in the prev if block
                    return False
                
                if d1[s[i]] == t[i]:
                    continue
                else:
                    return False
        return True
                
        