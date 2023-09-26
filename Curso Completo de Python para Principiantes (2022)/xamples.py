def minimum_degree_of_trio(n, edges):
    # Construir grafo
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = set()
        if v not in graph:
            graph[v] = set()
        graph[u].add(v)
        graph[v].add(u)

    min_degree = float('inf')

    # Iterar sobre nodos
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if j in graph[i]:
                for k in range(j + 1, n + 1):
                    if k in graph[i] and k in graph[j]:
                        degree = len(graph[i]) + len(graph[j]) + len(graph[k]) - 6
                        min_degree = min(min_degree, degree)

    return min_degree if min_degree != float('inf') else -1

# Ejemplo 1
n1 = 6
edges1 = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
output1 = minimum_degree_of_trio(n1, edges1)
print(output1)  # Output: 3

# Ejemplo 2
n2 = 7
edges2 = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
output2 = minimum_degree_of_trio(n2, edges2)
print(output2)  # Output: 0
