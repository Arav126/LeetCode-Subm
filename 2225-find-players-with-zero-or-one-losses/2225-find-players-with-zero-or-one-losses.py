class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        
        answer = [[],[]]
        
        # creating dict to find players who haven't lost
        
        dl = {}
        
        for i in matches:
            if i[1] not in dl:
                dl[i[1]] = 1
            elif i[1] in dl:
                dl[i[1]]+=1
                
            if i[0] not in dl:
                dl[i[0]] = 0
                
        print(dl)
        
        keyList = list(dl.keys())
        keyList.sort()
        for i in keyList:
            if dl[i] == 0:
                answer[0].append(i)
            elif dl[i] == 1:
                answer[1].append(i)
            
                
        print(answer)
        
        return answer
                
                
        