# https://www.geeksforgeeks.org/check-binary-tree-subtree-another-binary-tree-set-2/


class Node:
    def __init__(self, item):
        self.key = item 
        self.left = None
        self.right = None 

def storeInorder(root, arr):
    if root == None:
        arr.append('$')
        return 
    storeInorder(root.left, arr)
    arr.append(root.key)
    storeInorder(root.right, arr)

def storePreOrder(root, arr):
    if root == None:
        arr.append('$')
        return
    arr.append(root.key)
    storePreOrder(root.left, arr)
    storePreOrder(root.right, arr)


# this function returns true if S is a subtree of T; otherwise false
def isSubtree(T, S):
    if S == None:
        return True
    if T == None:
        return False

    inT = []
    inS = []
    storeInorder(T, inT)
    storeInorder(S, inS)
    if not ("".join(inS) in "".join(inT)): 
        return False
    
    preT = []
    preS = []
    storePreOrder(T, preT)
    storePreOrder(S, preS)
    
    return ("".join(preS) in "".join(preT))


T = Node('a')
T.left = Node('b')
T.right = Node ('d')
T.left.left = Node('c')
T.right.right = Node('e')

S = Node('a')
S.left = Node('b')
S.left.left = Node('c')
S.right = Node('d')

X = Node('x')
X.left = Node('y')

Y = Node('y')

# the subtree corresponding to the root node is the entire tree. 
# the subtree corresponding to any other node is called a proper subtree.
if (isSubtree(X,Y)):
    print("Yes: S is a subtree of W")
else:
    print("No: S is NOT a subtree of W")



