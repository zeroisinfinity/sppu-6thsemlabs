graph = {
    'A':[('B',4),('C',1)],
    'B':[('D',1)],
    'C':[('B',2),('D',5)],
    'D':[('E',5),('F',9)],
    'E':[('A',3),('B',9)],
    'F':[]
}


dist = {node : float('inf') for node in graph}

start = 'A'
dist[start] = 0
visited = set()


while len(visited) < len(graph):
    current = min(
                [x for x in graph if x not in visited],
                key = lambda x : dist[x]
            )

    visited.add(current)
    for neigh , wt in graph[current]:
        if dist[current] + wt < dist[neigh]:
            dist[neigh] = dist[current] + wt


print(dist)
print(graph)
