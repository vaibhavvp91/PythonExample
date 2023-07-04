from collections import deque

def bfs(graph):
    queue = deque()
    visited = set()
    
    for start_node in graph:
        if start_node not in visited:
            queue.append(start_node)
            
            while queue:
                node = queue.popleft()

                if node not in visited:
                    visited.add(node)
                    print(node)

                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            queue.append(neighbor)