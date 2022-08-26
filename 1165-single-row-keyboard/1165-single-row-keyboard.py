class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        ind = []
        
        for i in word:
            ind.append(keyboard.index(i))
            
        dist = abs(0-ind[0])
        for i in range(1,len(ind)):
            d = abs(ind[i-1]-ind[i])
            
            dist+=d
            
        return dist
        