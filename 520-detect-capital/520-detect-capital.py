class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        for i in word:
            if i != i.upper():
                break
        else:
            return True
        
        for i in word:
            if i != i.lower():
                break
        else:
            return True
        
        for i in range(len(word)):
            if word[0] != word[0].upper():
                break
            elif i!=0:
                if word[i] != word[i].lower():
                    break
        else:
            return True
        
        return False