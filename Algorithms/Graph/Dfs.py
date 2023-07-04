# Recursive
def dfs(graph):
    visited = set()

    for node in graph:
        if node not in visited:
            dfs_helper(graph, node, visited)

def dfs_helper(graph, node, visited):
    visited.add(node)
    print(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_helper(graph, neighbor, visited)	

# Iterative
def dfs(graph):
    stack = []
    visited = set()

    for start_node in graph:
        if start_node not in visited:
            stack.append(start_node)
            
            while stack:
                node = stack.pop()

                if node not in visited:
                    visited.add(node)
                    print(node)

                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            stack.append(neighbor)	
