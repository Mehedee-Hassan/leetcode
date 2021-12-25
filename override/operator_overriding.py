

# https://leetcode.com/problems/largest-number
# leetcode : 
class Compare(str):
        def __lt__(x,y):
            return x + y > y + x
    
class Solution:
    
    
    
    def largestNumber(self, nums: List[int]) -> str:
        test = [str(a) for a in nums]
        test = sorted( test ,key=Compare)
        
        test = ''.join(test)
        
        for z in test:
            if z != '0':
                return test
        return "0"
      
      
      
      
class weight:
  def __init__(self, weight):
    self. weight= weight
  def __lt__(self,other):
    return self.weight<other.weight
a=weight(50)
b=weight(60)
print(a<b)

