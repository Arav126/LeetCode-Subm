class Solution:
    def lengthOfLastWord(self, s: str) -> int:
#         s = [i for i in s]
#         s.reverse()
        
#         c=0
#         for i in range(0,len(s)):
#             if(s[i]!=' '):
#                 break
                
#         for j in range(i,len(s)):
#             if(s[i] == " "):
#                 break
#             else:
#                 c+=1
                
#         return c

        l = s.split(' ')
        while(1):
            if l[-1]=='':
                l.pop(-1)
            else:    
                return len(l[-1])
        