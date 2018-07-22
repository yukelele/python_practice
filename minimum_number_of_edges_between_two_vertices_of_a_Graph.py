class Queue:
    def __init__(self):
        self.size = 0
        self.Q = []

    def isEmpty(self):
        return True if self.size==0 else False

    def enqueue(self,data):
        self.Q.append(data)
        self.size += 1

    def dequeue(self):
        if self.isEmpty() == True:
            print("Queue is empty")
            return
        self.size -= 1
        return self.Q.pop(0)

def  minEdgeBFS(edges, u, v, n): #u--> source; v --> destination
    visited = [False] * n
    distance = [0] * n

    q = Queue()
    q.enqueue(u)
    visited[u] = True
    while(not q.isEmpty()):
        x = q.dequeue()
        for edge in edges[x]:
            if visited[edge]:
                continue
            distance[edge] = distance[x] + 1
            print("node", x, "| visiting", edge, "| distance", distance[x]+1)
            q.enqueue(edge)
            print("Queue:", q.Q)
            visited[edge] = True
            if edge==v:
                    return distance[v]
    return distance[v]
        

def addEdge(edges, u, v):
    edges[u].append(v)
    edges[v].append(u)

if __name__ == "__main__":
    n = 7 
    edges = [[] for i in range(n)]
    addEdge(edges,0,1)
    addEdge(edges,0,2)
    addEdge(edges,0,4)
    addEdge(edges,3,4)
    addEdge(edges,4,5)
    addEdge(edges,2,5)
    addEdge(edges,4,6)
    # addEdge(edges,3,4)
    # addEdge(edges,3,5)
    # addEdge(edges,4,5)
    # addEdge(edges,5,6)
    # addEdge(edges,6,7)
    # addEdge(edges,7,8)
    print(edges)
    u = 0
    v = 5 
    print(minEdgeBFS(edges,u,v,n))

    
