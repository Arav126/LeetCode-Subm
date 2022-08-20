class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        # Linear Search 
        
        for i in letters:
            if i > target:
                return i
            
        return letters[0] # if nothing is greater
            
        