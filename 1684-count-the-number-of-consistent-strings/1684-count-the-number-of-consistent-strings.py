class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        ret = 0
        for i in words:
            for j in i:
                if j not in allowed :
                    break
            else:
                # print(i,ret)
                ret+=1
                
        return ret