class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        li = s.split()
        ret = li[:k] #doesn't inc k
        ret = ' '.join(ret)
        
        return ret
        
        