class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = []
        ans.append(0)
        for i in range(0, len(gain)):
            j = gain[i] + ans[i]
            ans.append(j)
            
        return max(ans)
        