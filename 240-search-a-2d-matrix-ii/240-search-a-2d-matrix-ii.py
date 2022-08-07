class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        # n = matrix[i].length
        
        # for i in range(0, len(matrix)):
        #     if(target<=matrix[0][i]):
        #         i = i-1
        #         for j in range(0, len(matrix)):
        #             if(target == matrix[j][i]):
        #                 return True
        #         return False
        # return False
        
        for i in range(0, m):
            if target in matrix[i]:
                return True
            
        return False
        