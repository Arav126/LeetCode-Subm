class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        
#         l = [i for i in s]            #list comprehension
#         # print(l)
        
#         for i in range(0, len(s)):
#             if (l[i]=='0') :
#                 # print("i ran")
#                 continue
                
#             if (s[i] not in s[i+1:]): # complexity increased          #slicing here
#                 return i
#             else:
#                 # print(l.count(s[i]))
#                 for j in range(0, l.count(s[i])):
#                     # l.pop(l.index(s[i]))
#                     l[l.index(s[i])] = '0'
#             # print(l)
        
#         return -1

        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
                
        for i in s:
            if d[i] == 1:
                return s.index(i)
            
        return -1
            
        