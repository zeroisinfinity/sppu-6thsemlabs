import heapq

graph = {
'A':[('B',2),('C',4)],
'B':[('D',3)],
'C':[],
'D':[]
}

h = {
'A':6,
'B':2,
'C':5,
'D':0
}

start = 'A'
heap = [(h[start],0,start)]
g = {start:0}
came = {}
goal = 'D'

while heap:

    f , cost , current = heapq.heappop(heap)
    
    if goal == current:
        path = []
        while current in came:
            path.append(current)
            current = came[current]

        path.append(start)
        print(path[::-1])
        print('\n\n')
        print(g)
        break

    for neigh , wt in graph[current]:
        temp = g[current] + wt

        if neigh not in g or temp < g[neigh]:
            g[neigh] = temp
            came[neigh] = current

            heapq.heappush(
                        heap,
                        
                            (
                             h[neigh] + temp ,
                             temp,
                             neigh
                             )
                        
                    )


