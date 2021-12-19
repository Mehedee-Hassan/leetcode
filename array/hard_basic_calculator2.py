class Solution:
    
    def makeint(self,s):
        
        if s == "":
            return None
        
        i = 0
        
        for a in s:
            i = i*10 + (ord(a)-ord('0') )
        
        # print("num = ",i)
        return i
    
    def calc_op_next_number(self,prev_op,stack,temp_number):
        if prev_op == "*":
            stack.append(stack.pop() * temp_number)
        elif prev_op == "/":
            ome = stack.pop()
            stack.append(int(ome / temp_number))
                
                
            # print(ome,ome//temp_number,temp_number)
            # print(stack)

        elif prev_op == "+":
            stack.append(temp_number)
        elif prev_op == "-":
            stack.append(-temp_number)
        else:
            stack.append(temp_number)
            # first op sign just add the number
        # print(stack)
        
        
    
    def calculate(self, s: str) -> int:
        
        
        operators = set(["+","-","/","*"])
        stack = []
        
        
        new_expression_without_mul_div = []
        
        sarray = list(s)
        s_len = len(sarray)-1
        
        temps=[]
        prev_operator = None
        i = 0
        temp = []

        prev_op = None
        while  i <= s_len:
            if sarray[i] == " ":
                i += 1
                continue
                
            if sarray[i] not in operators:
                temp.append(sarray[i])
                
            else:
                   
                temp_number = self.makeint(temp)
                temp =[]
                
                if len(stack) > 0:
                    
                    self.calc_op_next_number(prev_op,stack,temp_number)
                    
                    prev_op = sarray[i]

                else:
                    stack.append(temp_number)
                    prev_op = sarray[i]
                
                
        
            
            i += 1
        
        # last val
        temp_number = self.makeint(temp)
        self.calc_op_next_number(prev_op,stack,temp_number)
            
        
        
        
        
#         print(stack)        
#         print(sum(stack))
        
        return sum(stack)
    
    
"""
"3+2*2"
" 3+5 / 2 "
" 3/2 "
"14-3/2"
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/836/

"""
