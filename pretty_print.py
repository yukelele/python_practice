class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right



def pretty_print(root):
    queue = []
    queue.append((root,0))
    while(queue):
        nodes = [queue.pop(0)]
        while(queue and nodes[0][1] == queue[0][1]):
            nodes.append(queue.pop(0))
        for node in nodes:
            print(node[0].val, end=" ")
            if node[0].left != None:
                queue.append((node[0].left, node[1]+1))
            if node[0].right != None:
                queue.append((node[0].right, node[1]+1))
        print("")


# Mistakes:
# 1. misusued varaible q, instead of queue
# 2. while(not queue) <-- while(queue) is correct because loop goes when there is something in the queue
# 3. comparing value in the current nodes set and queue value should be EQUAL! not unequal 
# 4. node in nodes is the tuple. node[0] is the actual node. node[1] is the depth 
#5. forgot to increment the depth 

if __name__ == "__main__":
    F = Node('f', None,None)
    A = Node('a', F, None)
    B = Node('b', None, None)
    C = Node('c', A, B)
    D = Node('d', C, None)

    pretty_print(D)