class DoctorNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class DoctorTree:
    def __init__(self):
        self.root = None
    def insert(self, parent_name, new_value, side, current_node=None):
        if self.root == None:
            return False

        if current_node is None:
            current_node = self.root

        if current_node.value == parent_name:
            if side == "left":
                if current_node.left is None: 
                    current_node.left = DoctorNode(new_value) 
                    print(f"{new_value} added under {parent_name} on the left.") 
                    return True 
                else:
                    print(f"{new_value} already has a left subordinate.")
                    return False
            elif side == "right":
                if current_node.right is None: 
                    current_node.right = DoctorNode(new_value) 
                    print(f"{new_value} added under {parent_name} on  the right.") 
                    return True
                else:
                     print(f"{parent_name} already has a right subordinate.")
                     return False
        if current_node.left and self.insert(parent_name, new_value, side, current_node.left):
            return True
        if current_node.right and self.insert(parent_name, new_value, side, current_node.right):
            return True

        if current_node is self.root:
            print(f"Parent node {new_value} not found in the tree")
        return False
    
    def preorder(self, node):
        if node is None: 
            return []
        return [node.value] + self.preorder(node.left) + self.preorder(node.right)
        
       
    
    def inorder(self, node):
        if node is None: 
            return []
        return self.inorder(node.left) + [node.value] + self.inorder(node.right)
      

        
    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.value] 

        
    
tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft") 

tree.insert("Dr. Croft", "Dr. Goldsmith", "right") 
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right") 
tree.insert("Dr. Phan", "Dr. Morgan", "left")
print(tree.preorder(tree.root)) 
print(tree.inorder(tree.root))
print(tree.postorder(tree.root))

