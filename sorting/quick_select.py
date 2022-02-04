import random
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        self.nums=nums
        self.k=k
        return self.quickselect(0,len(nums)-1)
        
        
    def partition(self,start,end):
        pivot_ind=random.randint(start,end)
        pivot=self.nums[pivot_ind]
        self.nums[pivot_ind],self.nums[end]=self.nums[end],self.nums[pivot_ind]
        
        pindex=start
        
        for i in range(start,end+1):
            if self.nums[i]>pivot:
                self.nums[i],self.nums[pindex]=self.nums[pindex],self.nums[i]
                pindex+=1
                
        self.nums[end],self.nums[pindex]=self.nums[pindex],self.nums[end]
        return pindex
        
        
    def quickselect(self,start,end):
        k=self.k -1
        if start<=end:
            
            pindex=self.partition(start,end)
            if pindex>k:
                return self.quickselect(start,pindex-1)
            elif pindex<k:
                return self.quickselect(pindex+1,end)
            else:
                print(self.nums)
                return self.nums[k]


print(Solution().findKthLargest([3,2,1,5,2,7,8],2))
