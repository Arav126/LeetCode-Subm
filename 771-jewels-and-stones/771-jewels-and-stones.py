class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        ret=0
        for i in jewels:
            for j in stones:
                if i == j:
                    ret+=1
        return ret