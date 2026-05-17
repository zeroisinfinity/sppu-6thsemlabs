# file: assignment1_bfs_dfs.py

from collections import deque

graph = {}


def add_edges():
    try:
        while True:
            u = input("Enter source node: ").strip()
            v = input("Enter destination node: ").strip()

            if not u or not v:
                print("Node cannot be empty")
                continue

            if u == v:
                print("Self-loop not allowed")
                continue

            graph.setdefault(u, [])
            graph.setdefault(v, [])

            if v in graph[u]:
                print("Edge already exists")
            else:
                graph[u].append(v)
                graph[v].append(u)
                print("Edge added")

            while True:
                ch = input("Add more edges? (yes/no): ").strip().lower()

                if ch in ["yes", "no" , '', 'y' , 'n']:
                    break

                print("Enter yes or no only")

            if ch in ["no",'n']:
                break

    except Exception as e:
        print("Error:", e)


def bfs():
    try:
        if not graph:
            print("Graph is empty")
            return

        start = input("Enter start node: ").strip()

        if not start:
            print("Node cannot be empty")
            return

        if start not in graph:
            print("Node not found")
            return

        visited = {start}
        queue = deque([start])

        print("BFS:", end=" ")

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print()

    except Exception as e:
        print("Error:", e)


def dfs_iter():
    try:
        if not graph:
            print("Graph is empty")
            return

        start = input("Enter start node: ").strip()

        if not start:
            print("Node cannot be empty")
            return

        if start not in graph:
            print("Node not found")
            return

        visited = set()
        stack = [start]

        print("DFS Iterative:", end=" ")

        while stack:
            node = stack.pop()

            if node not in visited:
                visited.add(node)
                print(node, end=" ")

                for neighbor in reversed(graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        print()

    except Exception as e:
        print("Error:", e)


def dfs_rec_util(node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_rec_util(neighbor, visited)


def dfs_rec():
    try:
        if not graph:
            print("Graph is empty")
            return

        start = input("Enter start node: ").strip()

        if not start:
            print("Node cannot be empty")
            return

        if start not in graph:
            print("Node not found")
            return

        print("DFS Recursive:", end=" ")
        visited = set()

        dfs_rec_util(start, visited)

        print()

    except RecursionError:
        print("Graph too deep for recursive DFS")

    except Exception as e:
        print("Error:", e)


def display_graph():
    try:
        if not graph:
            print("Graph is empty")
            return

        print("\nGraph:")
        for node, neighbors in graph.items():
            print(f"{node} -> {neighbors}")

    except Exception as e:
        print("Error:", e)


def main():
    while True:
        try:
            print("\n------ MENU ------")
            print("1. Add Graph")
            print("2. BFS")
            print("3. DFS Iterative")
            print("4. DFS Recursive")
            print("5. Display Graph")
            print("6. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                add_edges()

            elif choice == "2":
                bfs()

            elif choice == "3":
                dfs_iter()

            elif choice == "4":
                dfs_rec()

            elif choice == "5":
                display_graph()

            elif choice == "6":
                print("Program exited")
                break

            else:
                print("Invalid choice")

        except KeyboardInterrupt:
            print("\nProgram interrupted")
            break

        except Exception as e:
            print("Unexpected error:", e)


if __name__ == "__main__":
    main()
