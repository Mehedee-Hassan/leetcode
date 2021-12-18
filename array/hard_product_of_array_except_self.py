 class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # 1. there is 0 in the list
        onlyone_pro = 1
        
        start_to_end_array = [1] * len(nums)
        end_to_start_array = [1] * len(nums)
        
        start_to_end_array[0] =nums[0]
        end_to_start_array[-1] =nums[-1]
        
        
        end = len(nums)-1
        i = 1
        while ( i < len(nums)-1):
            start_to_end_array[i] = start_to_end_array[i-1] * nums[i]
            end_to_start_array[end-i] = end_to_start_array[end-i+1] * nums[end-i]
            
            
            
            i +=1
        
        
        # print(end_to_start_array)
        
        
        res = []
        i = 0 
        while i < len(nums):
            
            temp = 1
            if i != 0:
                temp *=start_to_end_array[i-1]
 
            if i != len(nums)-1:
                temp *= end_to_start_array[i+1]
            
            res.append(temp)
            
        
            
            i +=1
            
            
        return res
        
