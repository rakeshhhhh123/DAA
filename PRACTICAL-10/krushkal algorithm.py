edges = []

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

for i in range(e):
    u, v, w = input("Enter edge (u v weight): ").split()
    edges.append((int(w), u, v))

edges.sort()

parent = {}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y)

vertices = set()

for w, u, v in edges:
    vertices.add(u)
    vertices.add(v)

for v in vertices:
    parent[v] = v

cost = 0

print("Edges in Minimum Spanning Tree:")

for w, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        print(u, "-", v, ":", w)
        cost += w

print("Minimum Cost:", cost


