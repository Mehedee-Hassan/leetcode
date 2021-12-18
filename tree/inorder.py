        node =root
        
        stack =[]
        found = True
        while node != None or len(stack) > 0:
            
            
            
            while node != None:
                
                stack.append(node)
                node = node.left
                
            node= stack.pop()
            print(node.val)
            
            if found == False:
                return node
            if node.val ==p.val:
                found = False
            node = node.right
