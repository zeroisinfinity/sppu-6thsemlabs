import heapq

graph = {
'A':[('B',1),('C',4)],
'B':[('A',1),('C',2),('D',5)],
'C':[('A',4),('B',2),('D',1)],
'D':[('B',5),('C',1)]
}

heap = [(0,'A')]
visited = set()
cost = 0

while heap:
    wght , node = heapq.heappop(heap)
    
    if node in visited:
        continue
    cost += wght

    visited.add(node)

    for neigh , wt in graph[node]:
        if neigh not in visited:
            heapq.heappush(
                    heap,
                    (wt,neigh)
                    )



print(cost)
