# ============================================================
# QUESTION:
# Implement Kruskal's Minimum Spanning Tree Algorithm
# using Greedy approach.
# ============================================================


# ============================================================
# EXPLANATION:
#
# Kruskal's Algorithm finds Minimum Spanning Tree (MST)
# of a graph.
#
# MST:
# A subset of edges connecting all vertices
# with minimum total weight.
#
# Steps:
#
# 1. Sort edges in ascending order of weight.
# 2. Pick smallest edge.
# 3. Check if it forms cycle.
# 4. If no cycle → include edge.
# 5. Repeat until MST formed.
#
# Disjoint Set is used to detect cycles.
# ============================================================


# ============================================================
# EXPLANATION WITH EXAMPLE:
#
# Edges:
#
# (0,1,10)
# (0,2,6)
# (0,3,5)
# (1,3,15)
# (2,3,4)
#
# After sorting:
#
# (2,3,4)
# (0,3,5)
# (0,2,6)
# (0,1,10)
# (1,3,15)
#
# MST formed:
#
# (2,3,4)
# (0,3,5)
# (0,1,10)
#
# Total Cost = 19
# ============================================================


# ======================
# KRUSKAL PROGRAM
# ======================

class DisjointSet:

    def __init__(self, n):

        self.parent = list(range(n))


    def find(self, node):

        if self.parent[node] != node:

            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]


    def union(self, u, v):

        root_u = self.find(u)

        root_v = self.find(v)

        if root_u != root_v:

            self.parent[root_v] = root_u

            return True

        return False


def kruskal(n, edges):

    edges.sort(key=lambda x: x[2])

    ds = DisjointSet(n)

    mst = []

    total_cost = 0


    for u, v, weight in edges:

        if ds.union(u, v):

            mst.append((u, v, weight))

            total_cost += weight


    return mst, total_cost


# Driver Code

edges = [

    (0, 1, 10),

    (0, 2, 6),

    (0, 3, 5),

    (1, 3, 15),

    (2, 3, 4)

]

mst, cost = kruskal(4, edges)

print("MST:", mst)

print("Total Cost:", cost)