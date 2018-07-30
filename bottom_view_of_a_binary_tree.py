INT_MAX = float("inf")

class Node:
    def __init__(self, key):
        self.data = key
        self.hd = INT_MAX # hd = horizontal distance
        self.left = None
        self.right = None

def bottomView(root):
    if root == None:
        return 

    hd = 0
    m = {} # dictionary which stores key value pair sorted on key value
    q = [] # queue to store tree nodes in level order traversal 

    root.hd = hd
    q.append(root)

    while(q):
        temp = q.pop(0)

        hd = temp.hd

        m[hd] = temp.data

        if temp.left != None:
            temp.left.hd = hd - 1
            q.append(temp.left)

        if temp.right != None:
            temp.right.hd = hd + 1
            q.append(temp.right)

    for x in sorted(m):
        print(m[x], end=" ")
    print("")



root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
bottomView(root)