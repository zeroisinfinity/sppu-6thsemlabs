class Disjoints:
    def __init__(self,n):
        self.parent = list(range(n))

    def find(self,node):
        if self.parent[node] != node:
            node = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self,u,v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            self.parent[v] = root_u
            return True
        return False

def krushkal(n,edges):
    ds = Disjoints(n)
    cost = 0
    mst = []
    edges.sort(key = lambda x : x[2])

    for u , v , wt in edges:
        if ds.union(u,v):
            mst.append((u,v,wt))
            cost += wt

    return mst , cost

edges = [
(0,1,1),
(2,3,1),
(1,2,2),
(0,2,4),
(1,3,5)
]

print(krushkal(4,edges))
