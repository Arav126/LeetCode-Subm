class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        # sub with 97
        ret = []
        for i in words:
            temp = ''
            for j in i:
                temp+=morse[ord(j)-97]
                
            ret.append(temp)
            
        s = set(ret)
        
        return len(s)