class Solution:
    
    
    def backtrack(self,nums,q,current,vis):
        
        if len(vis) == len(nums):
            self.result.append(q.copy())
            q = []
            vis = set()
            return
        
        i = 0
        while i < len(nums):
            if nums[i] not in vis:
                vis.add(nums[i])
                q.append(nums[i])

                self.backtrack(nums,q,i,vis)

                q.pop(-1)
                vis.remove(nums[i])
            
            i += 1
    
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.result = []
        
        self.backtrack(nums,[],0,set())
        
        print(self.result)
        return self.result
