class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # ans = []
        # check = ["1","2","3","4","5","6","7","8","9"]
        # # condition-1
        # for i in range(0, len(board)):
        #     temp = check
        #     for j in range(0, len(temp)):
        #         if temp[j] in board[i]:
        #             temp.pop(j)
        #     if len(temp)!=0 :
        #         return False
        
        
        
        for i in range(0,len(board)):
            l = []
            s = set()
            for j in board[i]:
                if j!=".":
                    # print(j)
                    l.append(j)
                    s.add(j)
            # print(len(l), " | ", len(s))
            if(len(l)!=len(s)):
                return False
            
        print("True-1")
        
        for i in range(0, len(board)):
            l = []
            s = set()
            for j in range(0, len(board)):
                if board[j][i] != ".":
                    # print(j)
                    l.append(board[j][i])
                    s.add(board[j][i])
            # print(len(l), " | ", len(s))
            if(len(l)!=len(s)):
                return False
            
        print("True-2")
        
        
        boxes = [[0 for i in range(0,len(board))] for j in range(0,len(board))]
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                boxes[i][j] = ((i//3) *3 + j//3)
                
        create = [[] for j in range(0, len(board))]
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                index = boxes[i][j]
                val = board[i][j]
                create[index].append(val)
                
        # print(create)
        for i in range(0, len(create)):
            l = []
            s = set()
            for j in range(0, len(create)):
                if create[i][j] != ".":
                    l.append(create[i][j])
                    s.add(create[i][j])
            # print(len(l), " | ", len(s))
            if(len(l)!=len(s)):
                return False
        print("True-3")
        return True
        
    
        
        
        
        
        
        
        
        
            
            
                    
        