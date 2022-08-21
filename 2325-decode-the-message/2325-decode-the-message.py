class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        d = {}
        # LetterForNo = lambda x: chr(x)
        
        it = chr(ord('a')-1)
        
        for i in key:
            
            if i.lower() not in d and i !=' ':
                it = chr(ord(it)+1)
                d[i.lower()] = it
                
        ret = ''
        
        for i in message:
            if i == ' ':
                ret+=' '
            else:
                ret+=d[i.lower()]

        return ret
        