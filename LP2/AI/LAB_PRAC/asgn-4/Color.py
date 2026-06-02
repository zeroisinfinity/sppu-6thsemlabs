graph = [
    [0,1,1,1],
    [1,0,1,0],
    [1,1,0,1],
    [1,0,1,0]
]

n = len(graph)
m = int(input("Enter no. of colors: "))

color = [0]*n


def is_safe(node,c):

    for k in range(n):

        if graph[node][k]==1 and color[k]==c:
            return False

    return True


def solve(node):

    if node==n:
        print(color)
        return True


    for c in range(1,m+1):

        if is_safe(node,c):

            color[node]=c

            if solve(node+1):
                return True

            color[node]=0

    return False


if not solve(0):
    print("No solution")
