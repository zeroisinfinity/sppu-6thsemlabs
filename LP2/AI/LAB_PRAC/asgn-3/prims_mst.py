graph = {
'A':[('B',1),('C',4)],
'B':[('A',1),('C',2),('D',5)],
'C':[('A',4),('B',2),('D',1)],
'D':[('B',5),('C',1)]
}

visited = {'A'}
cost = 0
while len(visited) < len(graph):
    mn = float('inf')

    for node in visited:
        for neigh , wt in graph[node]:
            if neigh not in visited and wt < mn:
                nxt = neigh
                mn = wt

    visited.add(nxt)
    cost+=mn

print(cost)
