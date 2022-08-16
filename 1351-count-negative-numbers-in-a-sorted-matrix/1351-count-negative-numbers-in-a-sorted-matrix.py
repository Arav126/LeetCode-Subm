class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        flatList = [item for subList in grid for item in subList if item<0]
        
        return len(flatList)
        