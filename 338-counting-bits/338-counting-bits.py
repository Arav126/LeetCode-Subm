class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = []
        for i in range(0, n+1):
            
            b = bin(i)
        
            l = [int(i) for i in b[2:]]
            ans.append(sum(l))
        
        return ans
        