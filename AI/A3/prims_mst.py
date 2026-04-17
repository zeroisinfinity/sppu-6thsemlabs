import heapq # import heapq min heap

def prims_mst(graph : dict , start: int):
    # initialize
    min_heap = [(0,start,-1)]
    visited = set()
    min_cost = 0
    min_edges = []
    n = len(graph)

    # run till min_heap is empty OR len(visited) < n:
    while min_heap and len(visited) < n:
        # list of tuples min_heap push to heapq and get min_weight edge by tuple unpacking
        weight , node , parent = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        min_cost += weight
        if parent != -1:
            min_edges.append((parent,node,weight))


        for w,neigh in graph[node]:
            if neigh not in visited:
                heapq.heappush(min_heap,(w,neigh,node))

    return min_cost , min_edges


graph = {
    0: [(2, 1), (3, 3)],
    1: [(2, 0), (1, 2), (4, 3)],
    2: [(1, 1), (5, 3)],
    3: [(3, 0), (4, 1), (5, 2)]
}

cost, edges = prims_mst(graph,0)
print(f"MST cost: {cost}")
print(f"Edges:    {edges}")

