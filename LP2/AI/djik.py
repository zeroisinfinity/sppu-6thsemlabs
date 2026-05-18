import heapq

graph = {
    'A':[('B',4),('C',1)],
    'B':[('D',1)],
    'C':[('B',2),('D',5)],
    'D':[]
}

visited = set()
dist = {node : float('inf') for node in graph}

heap = [(0,'A')]
dist['A'] = 0

while heap:
    wght , node = heapq.heappop(heap)

    if node in visited:
        continue
        
    visited.add(node)

    for neigh,wt in graph[node]:
        if dist[node] + wt < dist[neigh]:
            dist[neigh] = dist[node] + wt

            heapq.heappush(heap , (dist[neigh],neigh))


print(dist)









































