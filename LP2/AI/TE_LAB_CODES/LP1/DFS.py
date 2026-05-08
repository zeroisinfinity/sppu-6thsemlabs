# ============================================================
# QUESTION:
# Implement Depth First Search (DFS) algorithm
# using recursion to search all vertices of a graph.
# ============================================================


# ============================================================
# EXPLANATION:
#
# Depth First Search (DFS) is a graph traversal algorithm
# that explores as far as possible along each branch
# before backtracking.
#
# It uses RECURSION or STACK.
#
# Steps:
# 1. Start from root node.
# 2. Mark node as visited.
# 3. Visit first neighbor.
# 4. Continue visiting neighbors deeply.
# 5. Backtrack when no neighbors left.
#
# DFS is useful in:
# - Path finding
# - Cycle detection
# - Topological sorting
# ============================================================


# ============================================================
# EXPLANATION WITH EXAMPLE:
#
# Consider graph:
#
#        A
#      /   \
#     B     C
#    / \     \
#   D   E     F
#
# DFS starting from A:
#
# Step 1: Visit A
# Step 2: Go to B
# Step 3: Go to D
# Step 4: Backtrack to B
# Step 5: Go to E
# Step 6: Backtrack to A
# Step 7: Go to C
# Step 8: Go to F
#
# Final DFS Order:
# A B D E C F
# ============================================================


# ======================
# DFS PROGRAM
# ======================

graph = {
    'A' : ['B' , 'C'] , 
    'B' : ['D' , 'E'] ,
    'C' : ['F'] , 
    'D' : [] ,
    'E' : ['F'],
    'F' : [] 
}

visited = set()


def dfs(visited , graph , node):

    if node not in visited :
        print(node)
        visited.add(node)

        for neighbour in graph[node]:
                dfs(visited , graph , neighbour)
    
   
print("Following is DFS  Traversal:")
dfs(visited , graph , 'A')