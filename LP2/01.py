def dfs(visited, graph, node):
    """Performs Depth First Search (DFS) recursively."""
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph.get(node, []):
            dfs(visited, graph, neighbour)

def bfs(visited, graph, start_node):
    """Performs Breadth First Search (BFS) iteratively."""
    queue = [start_node]
    visited.add(start_node)

    while queue:
        current = queue.pop(0)
        print(current, end=" ")
        for neighbour in graph.get(current, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    print("Graph Traversal using DFS and BFS")
    n = int(input("Enter number of nodes: "))
    graph = {}

    # Build the graph
    for i in range(1, n + 1):
        edges = int(input(f"Enter number of edges for node {i}: "))
        graph[i] = []
        for j in range(edges):
            neighbor = int(input(f"  Enter node {i}'s neighbor {j + 1}: "))
            graph[i].append(neighbor)

    print("\nConstructed Graph (Adjacency List):")
    for node in graph:
        print(f"{node}: {graph[node]}")

    # DFS Traversal
    print("\nDFS Traversal starting from node 1:")
    dfs(set(), graph, 1)

    # BFS Traversal
    print("\n\nBFS Traversal starting from node 1:")
    bfs(set(), graph, 1)

if __name__ == "__main__":
    main()
