class Solution:
    def subtractProductAndSum(self, n: int) -> int:
#         summ=0
#         prod=1
        
#         while(n != 0):
#             j = n%10
#             summ+=j
#             prod*=j
            
#             n/=10
            
                
#         diff = prod-summ
#         return diff


        listMain = [int(i) for i in str(n)]
        summ = sum(listMain)
        prod = 1
        
        for i in listMain:
            prod*=i
            
        return prod-summ