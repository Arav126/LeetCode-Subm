class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#         str1, str2 = "", ""
        
#         for i in s:
#             str1=""
#             str!+=i
#             for j in range(0, len(s)):

        if len(s)!=len(t) : return False

        l = [i for i in s]
        
        for i in t:
            if i in l:
                l.pop(l.index(i))
                
        if len(l) == 0:
            return True
        else:
            return False
                