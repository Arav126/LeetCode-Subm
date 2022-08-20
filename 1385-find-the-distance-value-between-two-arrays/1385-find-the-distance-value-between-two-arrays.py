class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        # i have no clue why this question is under binary search
        ret = 0
        for i in arr1:
            for j in arr2:
                if abs(j-i) > d:
                    continue
                else:
                    break
            else:
                ret+=1
        return ret