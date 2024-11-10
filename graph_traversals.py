
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

def dfs_recursive(graph, vertex, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []

    visited.add(vertex)
    result.append(vertex)
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)
    
    return result

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            stack.extend(reversed(graph[vertex]))  # Reverse for correct order
    
    return result

# Example Usage
graph = {
    'a': ['b', 'c', 'd'],
    'b': ['a', 'e'],
    'c': ['a', 'f'],
    'd': ['a'],
    'e': ['b'],
    'f': ['c']
}

print("BFS:", bfs(graph, 'a'))
print("DFS (Recursive):", dfs_recursive(graph, 'a'))
print("DFS (Iterative):", dfs_iterative(graph, 'a'))

