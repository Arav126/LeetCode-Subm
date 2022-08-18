class Solution:
    def compress(self, chars: List[str]) -> int:
        
#         ret = []
#         for i in chars:
#             if i not in ret:
#                 ret.append(i)
#                 if chars.count(i) != 1:
#                     ret.append(str(chars.count(i)))
                    
#         print(ret)
#         chars = ret.copy()
#         return len(chars)

        c = 1 # for 'aaa', if activated only twice, so initial = 1
    
        input = ''.join(chars)
        s = ''
        for i in range(1,len(input)):
            if input[i-1]==input[i]:
                c+=1
            else:
                s+=input[i-1]
                if c>1:
                    s+=str(c)

                c = 1

        s+=input[-1]
        if c>1:
            s+=str(c)
            
        chars[:] = [i for i in s]
        
        # print(s)

        return len(s)
        