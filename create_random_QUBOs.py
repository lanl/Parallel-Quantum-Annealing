"""
© 2021. Triad National Security, LLC. All rights reserved.
This program was produced under U.S. Government contract 89233218CNA000001 for Los Alamos
National Laboratory (LANL), which is operated by Triad National Security, LLC for the U.S.
Department of Energy/National Nuclear Security Administration. All rights in the program are
reserved by Triad National Security, LLC, and the U.S. Department of Energy/National Nuclear
Security Administration. The Government is granted for itself and others acting on its behalf a
nonexclusive, paid-up, irrevocable worldwide license in this material to reproduce, prepare
derivative works, distribute copies to the public, perform publicly and display publicly, and to permit
others to do so.
"""

"""
Generates some random graphs and their associated Maximum Clique QUBOs
"""

import json
import networkx as nx
import random

def is_clique(G):
    """
    parameters: G (networkx.Graph() object)
    description: checks if the input graph is a clique
    return Boolean True/False
    """
    n = len(list(G.nodes()))
    m = len(list(G.edges()))
    if m == (n*(n-1))/2:#A complete graph has number of edges equal to n choose 2 for n nodes
        return True
    else:
        return False
def maximum_clique_qubo(G):
    """
    parameters: G (networkx.Graph() object), quad_weight (quadratic coefficient)
    description: Finds the maximum clique QUBO for the input graph
    return Q (dictionary) QUBO
    """
    Q = {}
    GC = nx.algorithms.operators.unary.complement(G)#complement of the graph
    A = 1
    B = 2
    for i in list(GC.nodes()):
        Q[(i, i)] = -A
    for a in list(GC.edges()):
        Q[a] = B
    return Q

CLIQUE = 40

complete = nx.complete_graph(CLIQUE)

file = open("embeddings/Advantage_system1.1/clique"+str(CLIQUE)+"_embedding.json", "r")
embeddings = json.load(file)
file.close()

def run(embeddings):
	p = 0.50#random graph density
	print(len(embeddings))
	tries = 0
	for rep in range(len(embeddings)):
		graph_density = 0.0
		G = nx.Graph()
		non_zero_nodes = [a[0] for a in list(G.edges())]+[a[1] for a in list(G.edges())]
		degrees = [val for (node, val) in G.degree()]
		while (graph_density==0.0) or (graph_density==1.0) or (nx.is_connected(G)==False) or (len(list(G.edges())) <= 2) or (is_clique(G.subgraph(non_zero_nodes))==True) or (max(degrees) < 2):
			G = nx.gnp_random_graph(CLIQUE, p)
			graph_density = nx.density(G)
			non_zero_nodes = [a[0] for a in list(G.edges())]+[a[1] for a in list(G.edges())]
			degrees = [val for (node, val) in G.degree()]
			tries += 1
			if tries > 10000:
				print(str(p)+" density failed!!!!")
				return -1
		file = open("random_QUBOs/graph_"+str(rep)+".txt", "w")
		file.write(str(list(G.edges())))
		file.close()
		
		QUBO = maximum_clique_qubo(G)
		file = open("random_QUBOs/"+str(rep)+".txt", "w")
		file.write(str(QUBO))
		file.close()
run(embeddings)
