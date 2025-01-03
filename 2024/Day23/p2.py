import networkx as nx
import numpy as np

G = nx.Graph()
for l in open('input.txt').read().split('\n'):
    conn1,conn2 = l.split('-')
    G.add_node(conn1)
    G.add_node(conn2)
    G.add_edge(conn1,conn2)

cliques = list(nx.find_cliques(G))
cliques.sort(key=lambda x: len(x))
longest = cliques[-1]
longest.sort()
print(','.join(longest))