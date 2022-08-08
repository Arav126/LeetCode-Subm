class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # l = [
        #     ",", " ",":", ".","@","#","_","[","]","{",
        # ]
        
        ret = []
        for i in s:
            if(i.isalnum() ):
                ret.append(i)
                
        orig = ''.join(ret)
        ret.reverse()
        rev = ''.join(ret)
        
        print(orig.lower(), " | ", rev.lower())
        if orig.lower() == rev.lower():
            return True
        else:
            return False
        