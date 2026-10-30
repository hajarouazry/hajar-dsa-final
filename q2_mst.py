# ===== Question 2: Minimum Spanning Tree (Prim's algorithm) =====

import networkx as nx 
import matplotlib.pyplot as plt
from networkx import Graph

# ===== Part (a): Create and depict the original connected graph =====

# first graph: 6 nodes (A to F) and 11 weighted edges.
G1 = nx.Graph()
G1.add_edge("A", "B", weight= 5)
G1.add_edge("B", "C", weight= 3)
G1.add_edge("C", "D", weight= 11)
G1.add_edge("D", "E", weight= 4)
G1.add_edge("E", "F", weight= 7)
G1.add_edge("B", "D", weight= 2)
G1.add_edge("A", "C", weight= 9)
G1.add_edge("A", "F", weight= 6)
G1.add_edge("B", "E", weight= 8)
G1.add_edge("C", "F", weight=10)
G1.add_edge("D", "F", weight= 1)

print("Nodes:", G1.number_of_nodes())
print("Edges:", G1.number_of_edges())

# Draw the graph with edge weights and node letters (Original Graph G1)
def draw_graph(graph, title, seed=1):
    pos = nx.spring_layout(graph, seed=seed)
    nx.draw(graph, pos, with_labels=True, node_color="lightblue", node_size=800)
    weights = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=weights)
    plt.title(title)
    plt.show()

draw_graph(G1, "Original Graph G1")

# ==== Part (b): Prim's algorithm to find the MST

# Build the MST using the Prim's algorithm: start from one node, repeatedly add the cheapest to a new node, and print each step 
def MyMinimumSpanningTree(Graph) -> Graph:
    print("MST algorithm: Prim's")
    mst = nx.Graph()
    start = list(Graph.nodes)[0]
    visited = {start}
    step = 1
    while len(visited) < Graph.number_of_nodes():
        best_edge = None
        best_weight = 999
        for u in visited:
            for v in Graph.neighbors(u):
                if v not in visited: 
                    w = Graph[u][v]["weight"]
                    if w < best_weight:
                        best_weight = w
                        best_edge = (u, v)
        u, v = best_edge
        mst.add_edge(u, v, weight=best_weight)
        visited.add(v)
        print("Step", step, ": add edge:", u, "-", v, "with weight:", best_weight)
        step = step + 1
    return mst
mst1 = MyMinimumSpanningTree(G1) # calls the MST function on the first graph G1 

# ===== Part (c): Depict the final MST and print its total weight ======

print("Total weight of the MST:", mst1.size(weight="weight"))
draw_graph(mst1, "MST of G1")

# ===== Testing: graph G2 =====

# second graph (testing): 5 nodes (P to T) and 8 weighted edges.
G2 = nx.Graph()
G2.add_edge("P", "Q", weight= 3)
G2.add_edge("Q", "R", weight= 5)
G2.add_edge("R", "S", weight= 2)
G2.add_edge("S", "T", weight= 9)
G2.add_edge("P", "R", weight= 4)
G2.add_edge("P","T", weight= 8)
G2.add_edge("Q", "S", weight= 10)
G2.add_edge("R", "T", weight= 6)
print("G2 nodes:", G2.number_of_nodes(), "edges:", G2.number_of_edges())

draw_graph(G2, "Original graph G2")
mst2 = MyMinimumSpanningTree(G2)
print("Total weight of the MST:", mst2.size(weight="weight"))
draw_graph(mst2, "MST of G2")

# ===== Testing: graph G3 =====

# third graph (testing): 7 nodes (H to N) and 10 weighted edges, two groups joined by two bridges.
G3 = nx.Graph()
G3.add_edge("H", "I", weight= 1)
G3.add_edge("I", "J", weight= 3)
G3.add_edge("H", "J", weight= 5)
G3.add_edge("K", "L", weight= 4)
G3.add_edge("L", "M", weight= 10)
G3.add_edge("M", "N", weight= 6)
G3.add_edge("K", "N", weight= 2)
G3.add_edge("L", "N", weight= 8)
G3.add_edge("I", "L", weight= 7)
G3.add_edge("J", "K", weight= 9)
print("G3 nodes:", G3.number_of_nodes(), "edges:", G3.number_of_edges())

draw_graph(G3, "Original graph G3", seed=5)
mst3 = MyMinimumSpanningTree(G3)
print("Total weight of the MST:", mst3.size(weight="weight"))
draw_graph(mst3, "MST of G3")


            







      


            
