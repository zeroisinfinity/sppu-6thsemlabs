# ============================================================
# QUESTION:
# Implement Breadth First Search (BFS) algorithm.
# Use an Undirected Graph and develop an algorithm
# for searching all vertices of a graph or tree.
# ============================================================


# ============================================================
# EXPLANATION:
#
# Breadth First Search (BFS) is a graph traversal algorithm
# that visits nodes level by level.
#
# It uses a QUEUE data structure.
#
# Steps:
# 1. Start from the initial node.
# 2. Add it to visited list and queue.
# 3. Remove first element from queue.
# 4. Visit all unvisited neighbors.
# 5. Repeat until queue becomes empty.
#
# BFS ensures that the shortest path is found
# in unweighted graphs.
# ============================================================


# ============================================================
# EXPLANATION WITH EXAMPLE:
#
# Consider the graph:
#
#        A
#      /   \
#     B     C
#    / \     \
#   D   E     F
#
# BFS traversal starting from A:
#
# Step 1: Visit A
# Queue = [A]
#
# Step 2: Visit neighbors B, C
# Queue = [B, C]
#
# Step 3: Visit B → Add D, E
# Queue = [C, D, E]
#
# Step 4: Visit C → Add F
# Queue = [D, E, F]
#
# Step 5: Visit D → E → F
#
# Final BFS Order:
# A B C D E F
# ============================================================


# ======================
# BFS PROGRAM
# ======================    
graph = {
    'A' : ['B' , 'C'] , 
    'B' : ['D' , 'E'] ,
    'C' : ['F'] , 
    'D' : [] ,
    'E' : ['F'],
    'F' : [] 
}

visited = []
queue = []

def bfs(visited , graph , node):
    visited.append(node)
    queue.append(node)

    while queue:
            s = queue.pop(0)
            print(s , end=" ")

            for neighbour in graph[s]:
                  if neighbour not in visited :
                        visited.append(neighbour)
                        queue.append(neighbour)


bfs(visited , graph , 'A')