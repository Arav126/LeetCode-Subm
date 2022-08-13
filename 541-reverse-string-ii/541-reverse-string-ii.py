class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = [i for i in s]
        ret = []
        inc = int(k)
        for i in range(0, len(l), inc):
            ret.append(l[i:i+inc])
                        
        for i in range(0, len(ret), 2):
            temp = ret[i]
            ret[i] = temp[::-1]
            
        # print(ret)
        flatListStr = [item for subList in ret for item in subList]
        # print(flatListInt)
        final = ''.join(flatListStr)
        return final
                
                
        # temp = l[i:i+k+1]
        #     ret.append(temp[::-1])
        #     ret.append(l[i+k+2:2k])
