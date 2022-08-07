class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        ans = []
        
        for i in range(0, len(sentences)):
            j=1
            for s in sentences[i]:
                if s == " ":
                    j+=1
            ans.append(j)
                
        return max(ans)