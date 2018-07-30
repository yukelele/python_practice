class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None 

# don't not print from left to right. Instead, print by level 
def topView(root):
    if root == None:
        return 

    m = {} # map
    q = [] # queue

    q.append((root,0)) # (node, horizontal distance)

    while(q): # while queue is not empty
        p = q.pop(0)
        node = p[0]
        val = p[1]

        # if horizontal value is not in the hashmap, then that means it is the first value with that horizontal distance 
        if val not in m: 
            m[val] = node.data
            print(node.data, end=" ")

        if node.left != None:
            q.append( (node.left, val-1) )
        
        if node.right != None:
            q.append( (node.right, val + 1 ))

            


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)

topView(root)
print("")