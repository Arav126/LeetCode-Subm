# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
import bisect
class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        # for i in range(0, n):
        #     if(isBadVersion(i)):
        #         return i
        # self.__getitem__ = isBadVersion()
        
        return bisect.bisect_left(self, True, 1, n)
    
    def __getitem__(self, key):
        return isBadVersion(key)
        