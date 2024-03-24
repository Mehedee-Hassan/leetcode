# https://leetcode.com/problems/contiguous-array/

class Solution:
    def if_one(self, val:int):
        if val == 1:
            return 1
        return -1

    def findMaxLength(self, nums: List[int]) -> int:
        
        map = {}
        map[0] = -1

        maxLen:int = 0
        count:int = 0

        i:int = 0
        while i < len(nums):
            
            count = count + self.if_one(nums[i])

            if count in map:
                maxLen = max(maxLen , i - map[count])

            else:
                map[count] = i
        

            i += 1

        return maxLen
