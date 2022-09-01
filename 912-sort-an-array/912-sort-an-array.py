class Solution:
    def merge(self,fh, sh, arr):
        i = 0
        j = 0
        k = 0

        while i < len(fh) and j < len(sh):
            if fh[i] < sh[j]:
                arr[k] = fh[i]
                i+=1
                k+=1
            else:
                arr[k] = sh[j]
                j+=1
                k+=1
        if i!=len(fh):
            while(i<len(fh)):
                arr[k] = fh[i]
                i+=1
                k+=1
        elif j!= len(sh):
            while(j<len(sh)):
                arr[k] = sh[j]
                j+=1
                k+=1

    def mergeSort(self,arr):
        if len(arr) == 1 or len(arr) == 0:
            return
        mid = len(arr)//2

        fh = arr[:mid]
        sh = arr[mid:]
        # print(fh, sh)
        self.mergeSort(fh)
        self.mergeSort(sh)

        # by now both our fh and sh are sorted now no recursion required

        self.merge(fh, sh, arr)
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # seems easy but it's asking us to sort an array in the fastest way possible
        # i.e merge sort not selection or bubble or any other sort
        
        self.mergeSort(nums)
        return nums
        