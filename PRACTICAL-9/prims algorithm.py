import heapq

graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    node = input("Enter vertex: ")
    graph[node] = []

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v, w = input("Enter edge (u v weight): ").split()
    w = int(w)

    graph[u].append((w, v))
    graph[v].append((w, u))

start = input("Enter starting vertex: ")

visited = set()
heap = [(0, start)]
cost = 0

while heap:
    weight, node = heapq.heappop(heap)

    if node in visited:
        continue

    visited.add(node)
    cost += weight

    if weight != 0:
        print(node, "added with weight", weight)

    for w, neighbour in graph[node]:
        if neighbour not in visited:
            heapq.heappush(heap, (w, neighbour))

if len(visited) == n:
    print("Minimum cost:", cost)
else:
    print("Graph is not connected")
