import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

g = defaultdict(list)
edg = []

with open('inputs/day25.txt') as file:
    for x in file:
        node, edges = x.split(': ')
        for edge in edges.split():
            g[node].append(edge)
            g[edge].append(node)
            edg.append((node, edge))

# G = nx.Graph(edg)

# pos = nx.spring_layout(G) 
# nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, font_color='black', edge_color='gray', linewidths=0.5)

# plt.show()
# # vbk-gqr
# # klj-scr
# # mxv-sdv
            
g["vbk"].remove("gqr")
g["gqr"].remove("vbk")
g["klj"].remove("scr")
g["scr"].remove("klj")
g["mxv"].remove("sdv")
g["sdv"].remove("mxv")

def size_of_components(g, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(g[node])
    return len(visited)

print(size_of_components(g, "vbk") * size_of_components(g, "scr"))

