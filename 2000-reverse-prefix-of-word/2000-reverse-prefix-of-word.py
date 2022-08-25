class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        li = [i for i in word]
        
        if ch in word:
            first = word.index(ch)
            last = word.rindex(ch)
            print(last)
            if len(ch)==1:
                last = first
        else:
            return word
        
        print(li)
        temp = li[0:last+1]
        print(temp)
        li[0:last+1] = temp[::-1]
        print(li)
        
        j = ''.join(li)
        return j
        
        