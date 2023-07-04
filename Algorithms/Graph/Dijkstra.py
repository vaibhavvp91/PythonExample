import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()
    previous = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous


def shortest_path(graph, start, end):
    distances, previous = dijkstra(graph, start)
    path = []
    current_node = end

    while current_node is not None:
        path.append(current_node)
        current_node = previous[current_node]

    path.reverse()
    return path


# Example usage:

# Create a graph represented as an adjacency dictionary
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 1},
    'D': {'B': 3, 'C': 1, 'E': 4},
    'E': {'D': 4}
}

start_node = 'A'
end_node = 'E'

shortest_distances, previous_nodes = dijkstra(graph, start_node)
shortest_path = shortest_path(graph, start_node, end_node)

print("Shortest distances from node", start_node + ":")
for node, distance in shortest_distances.items():
    print("To node", node + ":", distance)

print("Shortest path from", start_node, "to", end_node + ":")
print(shortest_path)
