class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        ret = []
        
        # XOR is using binary values
        # inverse of XOR is also XOR
        
        ret.append(first)
        
        for i in range(0,len(encoded)):
            ret.append(ret[i] ^ encoded[i])

        return ret
        