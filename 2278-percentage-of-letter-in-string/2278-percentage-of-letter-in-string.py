class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        l = [i for i in s]
        
        count = l.count(letter)
        
        perc = count*100/len(s)
        perc = floor(perc)
        return perc