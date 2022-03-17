import java.util.Stack;

class ScoreOfParentheses {
    public int getScoreOfParentheses(String s) {
        
        Stack<Integer> stack = new Stack<>();
        stack.push(0);
        
        
        for(char c: s.toCharArray()){
            
            if(c == '('){
                stack.push(0);
            }else{
                // we received a )
                
                // pop current () value
                int middle_sum = stack.pop();
                // pop last sum
                int last_sum= stack.pop();
                
                stack.push(last_sum + Math.max(2 * middle_sum ,1) );
                
                
            }
            
        }
        
        
    return stack.pop(); // all the elemnt should be popped till now
        
    }
}
