class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        d = {}
        
        for i in range(0, len(list1)):
            for j in range(0,len(list2)):
                if list1[i] == list2[j]:
                    ind = i+j
                    if ind not in d:
                        d[ind] = [list1[i]]
                    else:
                        d[ind].append(list1[i])
                        
        l = list(d.keys())
        mn = min(l)
        return d[mn]
        