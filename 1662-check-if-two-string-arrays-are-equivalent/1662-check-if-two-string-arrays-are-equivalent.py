class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ""
        str2 = ""
        
        for i in word1:
            # str1.append(i)
            str1 = str1 + i
            
        for i in word2:
            # str2.append(i)
            str2 = str2 + i
            
        if(str1 == str2):
            return True
        else:
            return False    
            
        