import heapq

def dijkstra(graph, start, debug=False):
    # Initialize all distances to infinity and path map
    distances = {node: float('inf') for node in graph}
    previous_nodes = {node: None for node in graph}
    distances[start] = 0

    # Min-heap priority queue
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if debug:
            print(f"Visiting {current_node} with current distance {current_distance}")

        # Skip if a shorter path was already found
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Found a shorter path to neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_nodes

def reconstruct_path(previous_nodes, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()
    if path[0] == start:
        return path
    return []

def print_all_paths(graph, start):
    distances, previous_nodes = dijkstra(graph, start)
    print(f"🔗 Shortest paths from {start}:\n")
    for node in graph:
        path = reconstruct_path(previous_nodes, start, node)
        if distances[node] < float('inf'):
            path_str = ' -> '.join(path)
            print(f"{node}: {path_str} (Cost: {distances[node]})")
        else:
            print(f"{node}: No path")

# Define the graph as an adjacency list
graph = {
    'A': [('B', 4), ('C', 5)],
    'B': [('A', 4), ('C', 11), ('D', 9), ('E', 7)],
    'C': [('A', 5), ('B', 11), ('E', 3)],
    'D': [('B', 9), ('F', 2)],
    'E': [('B', 7), ('C', 3), ('F', 6)],
    'F': [('D', 2), ('E', 6)]
}

# Run Dijkstra and print all paths from source node 'A'
print_all_paths(graph, 'A')
