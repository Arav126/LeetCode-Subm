class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        l = [item for subList in matrix for item in subList]
        print(l)
        l.sort()
        
        # didn't use the fact that they are sorted row wise
        
        
        return l[k-1]
            