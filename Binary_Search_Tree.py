class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
 
class BinarySearchTree:
    def __init__(self):
        self.root = None
 
    def insert(self, key):
        self.root=self._insert(self.root,key)
 
    def _insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self._insert(root.left,key)
        elif key > root.key:
            root.right=self._insert(root.right,key)
        return root
 
    def search(self, key):
        return self._search(self.root, key)
 
    def _search(self, root, key):
        if root is None or root.key==key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)
 
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key,end=" ")
            self.inorder(node.right)
 
    def preorder(self,node):
        if node:
            print(node.key,end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
 
 
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key,end=" ")

 
tree = BinarySearchTree()
elements = [50,70,80,60,90,40,20,30]
for el in elements:
    tree.insert(el)


print("Search 80:", tree.search(80).key if tree.search(80) else "Not Found")  
print("Search 90:", tree.search(90).key if tree.search(90) else "Not Found")   

print("\nInorder traversal:", end=" ")
tree.inorder(tree.root)     
print("\nPreorder traversal:", end=" ")
tree.preorder(tree.root)   
print("\nPostorder traversal:", end=" ")
tree.postorder(tree.root) 
print()