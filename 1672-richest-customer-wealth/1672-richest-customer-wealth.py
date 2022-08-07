class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        mx = sum(accounts[0])
        for i in range(0, len(accounts)):
            if(sum(accounts[i]) > mx):
                mx = sum(accounts[i])
                
        return mx
            
        