class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         for i in range(0, len(prices)-1): # buy here
#             for j in range(i+1, len(prices)): # sell here
#                 if(prices[j] - prices[i] > profit):
#                     profit = prices[j] - prices[i]
                    
#         return profit

#         profit = 0
#         ans = []
#         for i in range(0, len(prices)-1):
#             ans = prices[i+1:]
#             mx = max(ans)
#             if(mx-prices[i] > profit):
#                 profit = mx-prices[i]
                
#         return profit

#         profit = 0
#         ans = []
#         for i in range(0, len(prices)-1):
#             ans = prices[i+1:]
#             profit = max(max(ans)-prices[i], profit)
                
#         return profit

        # Decreasing half the test cases by using a minimum purchase criteria
        
        maxProfit = 0
        minPurchase = prices[0]
        
        for i in range(1, len(prices)):
            maxProfit = max(prices[i]-minPurchase, maxProfit)
            minPurchase = min(prices[i], minPurchase)
            
        return maxProfit
    
        