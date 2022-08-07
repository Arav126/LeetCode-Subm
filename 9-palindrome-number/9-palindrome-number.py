class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if(x<0):
            return False
        
        l = [int(i) for i in str(x)]
        print(l)
        rev = l[::-1]
        print(rev)
        
        if(l == rev):
            return True
        else:
            return False
        