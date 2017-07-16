#There must be no duplicate nodes. Point to be noted in BST

class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
    

def search(root,key):
    if root is None or root.data == key:
        return root
    
    if root.data < key:
        search(root.right, key)
        
    return search(root.left, key)

#A new key is always inserted at the leaf

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
'''
Time Complexity: The worst case time complexity of search and insert operations is O(h) where h is height of Binary Search Tree. In worst case, we may have to travel from root to the deepest leaf node. The height of a skewed tree may become n and the time complexity of search and insert operation may become O(n).
'''

#Delete
'''
1) Node to be deleted is leaf: Simply remove from the tree
2) Node to be deleted has only one child: Copy the child to the node and delete the child
3) Node to be deleted has two children: Find inorder successor of the node. Copy contents of the inorder successor to the node and delete the inorder successor. Note that inorder predecessor can also be used.In this particular case, inorder successor can be obtained by finding the minimum value in right child of the node.
'''

#insert
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def minvalnode(root):
    current = root
    while current.left is not None:
        current = current.left
    return current

def deletenode(root,key):
    if root is None:
        return root
    
    if key < root.data:
        root.left = deletenode(root.left, key)
    
    elif key > root.data:
        root.right = deletenode(root.right, key)
        
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        temp = minvalnode(root.right)
        root.data = temp.data
        root.right = deletenode(root.right, temp.data)
    return root

'''
The worst case time complexity of delete operation is O(h) where h is height of Binary Search Tree. In worst case, we may have to travel from root to the deepest leaf node. The height of a skewed tree may become n and the time complexity of delete operation may become O(n)
'''

