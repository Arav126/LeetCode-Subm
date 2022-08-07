class Solution:
    def sortSentence(self, s: str) -> str:
        
        words = s[::-1].split()
        words.sort()
        
        res = []
        for i in words:
            res.append(i[1:][::-1]) # woah
            
        res = ' '.join(res)
        return res
            
        