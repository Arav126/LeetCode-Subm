class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
#         uniq = list(set(arr))
#         sz = []
        
#         if(len(uniq) == 1):
#             return 1
        
#         for i in range(len(uniq)):
#             for j in range(i+1,len(uniq)):
#                 temp = arr.copy()
                
#                 for k in range(temp.count(uniq[i])):
#                     temp.pop(temp.index(uniq[i]))
#                 for k in range(temp.count(uniq[j])):
#                     temp.pop(temp.index(uniq[j]))
                        
#                 # print(temp)
                        
#                 sz.append(len(temp))
                    
#         ret = [i for i in sz if i<(len(arr)//2)]
#         print(sz)
#         print(ret)
#         return len(ret)

        # n is just no. of numbers to be popped
    
        d = {}
        
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
                
        it = list(d.values())
        it.sort()
        it.reverse()
        
        half = len(arr)//2
        ret = 0
        i = 0
 
        # while(len(arr)>half):
#             key = list(d.keys())[list(d.values()).index(it[i])]

#             for j in range(arr.count(key)):
#                 arr.pop(arr.index(key))
#             d.pop(key)
#             ret+=1

#             i+=1

        s = len(arr)
        for i in range(len(it)):
            if s <= half:
                break
                
            s-=it[i]
            ret+=1
                
            
            
        return ret