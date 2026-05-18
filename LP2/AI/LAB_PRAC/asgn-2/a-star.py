graph = {
        'A' : [('B',4) , ('C',3)],
        'B' : [('D',2)]
}

hue = {
        'A' : 7,
        'B' : 3,
        'C' : 8,
        'D' : 0
}



def a_star(goal:str):
    start = 'A'
    open_set = [(start,0)]
    came = dict()
    g = {start:0}

    while open_set:
        current = min(
            open_set,
            key = lambda x : x[1] + hue[x[0]]
            )[0]


        if current == goal:
            path = []

            while current in came:
                path.append(current)
                current = came[current]
        
            path.append(start)
            path.reverse()

            print(path)
            print(g[goal])
            return

        open_set = [x for x in open_set if x[0] != current]

        for neigh,wt in graph[current]:
        
            temp = g[current] + wt

            if neigh not in g or temp < g[neigh]:
                g[neigh] = temp
                came[neigh] = current

            if neigh not in [x[0] for x in open_set]:
                open_set.append((neigh,temp))

a_star('D')



























