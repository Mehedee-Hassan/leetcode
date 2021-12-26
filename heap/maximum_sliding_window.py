 import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        
        i = 0
        while i < len(nums):
            nums[i] = (-1) * nums[i]
            i += 1
        
        # print(nums)
        
        i = 0
        temp = []
        while i < k:
            
            temp.append((nums[i],i))
            
            
            i += 1
            
        pq = heapq.heapify(temp)
        test = heapq.heappop(temp)
        
        res = []
        res.append(test[0])
        
        if test[1] > 0:
            heapq.heappush(temp,test)

        
        i = 1
        j = k
        while j < len(nums):
            
            # print(nums[j])
            heapq.heappush(temp,(nums[j],j))
            
            # print(temp)
            while temp:
                
                test = heapq.heappop(temp)
                # print(test)
                if test[1] >= i:
                    # print(test[1])
                    res.append(test[0])
                    
                    if test[1] > i:
                        heapq.heappush(temp,test)
                    
                    break
                
            j += 1
            i += 1
        
        
        # print(res)
        
        i = 0
        while i < len(res):
            res[i] = (-1) * res[i]
            i += 1
        
        return res
            
        
        
"""
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

"""

#https://leetcode.com/problems/sliding-window-maximum/
