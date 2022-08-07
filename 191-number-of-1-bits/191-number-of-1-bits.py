class Solution:
    def hammingWeight(self, n) -> int:
        
        return str(bin(n)).count('1')
        