class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
#         # building a dictionary
#         d = {}
        
#         for i in words:
#             if i not in d:
#                 d[i] = 1
#             else:
#                 d[i]+=1
                
#         sv = list(d.values())
#         sv.sort()
#         sv.reverse()
        
#         ret = []
        
#         for i in range(k):
#             val = list(d.keys())[list(d.values()).index(sv[i])]
#             ret.append(val)
#             d.pop(val)
            
#         return ret
    
#     # not able to do lexicographic order

        # building a double dictionay will work
    
        freq = {}
        
        for i in words:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1
                
        dist = {}
        
        # it = list(d.keys())
        # it.sort()
        # it.reverse()
        
        for i in range(len(list(freq.values()))):
            val = list(freq.keys())[i]
            j = list(freq.values())[i]
            if j not in dist :
                dist[j] = [val]
            else:
                dist[j].append(val)
                
        # print(freq)
        # print(dist)
        
        #lexographic sort
        
        for i in dist:
            temp = dist[i]
            temp.sort()
            # temp.reverse()
            dist[i] = temp
            
        it = list(dist.keys())
        it.sort()
        it.reverse()
        
        ret = []
        for i in it:
            ret.extend(dist[i])
            
        # print(ret)
        
        return ret[:k]
            
            
        
        