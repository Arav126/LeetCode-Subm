class Solution:
    def average(self, salary: List[int]) -> float:
        mx = max(salary)
        mn = min(salary)
        
        # for i in range(0, len(salary)):
            # if(salary[i] == mx or salary[i] == mn):
                # salary.pop(i)
        
#         for i in salary:
#             if(i == mx or i == mn):
#                 salary.pop(salary.index(i))
                
#         if len(salary) == 1:
#             return salary[0]
#         else:
#             return sum(salary)/len(salary)

        salary.pop(salary.index(mx))
        salary.pop(salary.index(mn))
        
        avg = sum(salary)/len(salary)
        return avg
                
        
        