class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        for i in range(0,len(candies)):
            j = candies[i]+extraCandies
            if(j >= max(candies)):
                ans.append(True)
            else:
                ans.append(False)
        return ans            
        