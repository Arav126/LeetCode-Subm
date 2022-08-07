class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(len(nums) ==1):
            return nums
        
        i = 0
        while(i!=k):
            j = nums.pop()
            nums.insert(0,j)
            
            i+=1
            
            # if(i==k):
            #     break
                
        return nums
        