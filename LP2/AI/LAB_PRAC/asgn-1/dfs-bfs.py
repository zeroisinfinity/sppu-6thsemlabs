from collections import deque

graph = {
        1 : [2,3],
        2 : [1,4],
        3 : [1],
        4 : [2]
        }

def add_edges():
    
    try:
        while True:

            u = input("Enter source node: ").strip()
            v = input("Enter dest node: ").strip()

            while not u or not v:
                print("Nodes can't be empty")
                add_edges()

            while u == v:
                print("Self loop not allowed.")
                add_edges()

            u = int(u) ; v = int(v)

            graph.setdefault(u,[])
            graph.setdefault(v,[])
    
            if v in graph[u]:
                print("node already exists")
            else:
                graph[u].append(v)
                graph[v].append(u)

            while True:
                ch = input("Enter wanna continue? (y/n): ").strip().lower()

                if ch in ['y','n','yes','no','']:
                    break
                else:
                    print("Enter valid option")

            if ch in ['n','no']:
                break
    except Exception as e_msg:
        print('Exception: {}'.format(e_msg))



def bfs(graph: dict):

    try:
        if not graph:
            print('Graph is emtpy\nbfs => empty')
            return

    
        while True:
            start = input('Enter starting point: ').strip()
            
            if not start:
                print('Cant be empty')
            
            elif int(start) not in graph:
                print('Node not in graph. Try different one.')

            else:
                start = int(start)
                break

        visited = {start}
        queue = deque([start])

        while queue:
            node = queue.popleft()
            print(node, end=' ')

            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append(neigh)

        print()

    except Exception as e_msg:
        print(f'Exception: {e_msg}')


def dfs_iter(graph:dict):
    
    try:
        if not graph:
            print('Graph is emtpy\ndfs => empty')
            return

    
        while True:
            start = input('Enter starting point: ').strip()

            if not start:
                print('Cant be empty')

            elif int(start) not in graph:
                print('Node not in graph. Try different one.')

            else:
                start = int(start)
                break

        visited = {start}
        stack = [start]

        while stack:
            node = stack.pop()
            print(node, end=' ')

            for neigh in reversed(graph[node]):
                if neigh not in visited:
                    visited.add(neigh)
                    stack.append(neigh)

        print()

    except Exception as e_msg:
        print(f'Exception: {e_msg}')

def dfs_rec(graph:dict):

    try:
        if not graph:
            print('Graph is emtpy\ndfs => empty')
            return

    
        while True:
            start = input('Enter starting point: ').strip()

            if not start:
                print('Cant be empty')

            elif int(start) not in graph:
                print('Node not in graph. Try different one.')

            else:
                start = int(start)
                break

        visited = {start}
        dfs_rec_util(start,visited)

        print()

    except Exception as e_msg:
        print(f'Exception: {e_msg}')



def dfs_rec_util(node:int,visited:set):

    print(node,end=' ')

    for neigh in graph[node]:
        if neigh not in visited:
            visited.add(neigh)
            dfs_rec_util(neigh,visited)



dfs_iter(graph)
bfs(graph)
dfs_rec(graph)
