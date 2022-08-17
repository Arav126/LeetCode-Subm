class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        l = [item for subList in matrix for item in subList]
        print(l)
        l.sort() # no need to sort since, it's already given in sorted mannar
        
        
        return l[k-1]
            