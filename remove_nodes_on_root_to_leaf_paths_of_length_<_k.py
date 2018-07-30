class Node:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None 


def removeShortPathNodesUtil(root, level, k):
    if root == None:
        return None

    #traverse the tree in postorder fashion so that if a leaf node path length is shorter than k,
    # then that node and all of its descendants till the node which are not on some other path are removed 
    root.left = removeShortPathNodesUtil(root.left, level+1, k)
    root.right = removeShortPathNodesUtil(root.right, level+1, k)

    # If root is a leaf node and its level is less than k then remove this node
    # this goes up and check for the ancestor nodes also for the same condition till it finds a node which is a part of other path(s) too 
    if root.left == None and root.right == None and level < k:
        del root
        return None
    
    return root

def removeShortPathNodes(root, k):
    pathLen = 0
    return removeShortPathNodesUtil(root,1,k)

def printInorder(root):
    if(root):
        printInorder(root.left)
        print(root.data, end=" ")
        printInorder(root.right)
    

k = 4
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
root.right.right = Node(6)
root.right.right.left = Node(8) 

printInorder(root)
print("")
res = removeShortPathNodes(root,k)
printInorder(res)
print("")

#Time complexity = O(n) where n is number of nodes in given Binary Tree 