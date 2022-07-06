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
Calls the Networkx solver to find all maximum cliques (if there are degenerate ground state solutions)
This data is required when computing the resulting ground state probability (GSP) of the saved D-Wave results
"""

import math
from dwave import embedding
import ast
import itertools
import time
import networkx as nx
from dwave.cloud import Client
import json
import random
import dimod

def get_Max_Cliques(G):
                MC_numb = nx.graph_clique_number(G)
                cliques = [a for a in nx.algorithms.clique.find_cliques(G)]
                MC = []
                for c in cliques:
                        if len(c) == MC_numb:
                                MC.append(c)
                return MC

CLIQUE = 40

file = open("embeddings/Advantage_system1.1/clique"+str(CLIQUE)+"_embedding.json", "r")
embeddings = json.load(file)
file.close()

for problem in range(len(embeddings)):
	file = open("random_QUBOs/graph_"+str(problem)+".txt", "r")
	G = nx.Graph(ast.literal_eval(file.read()))
	file.close()
	
	minimum_vectors = []
	MCs = get_Max_Cliques(G)
	for MC in MCs:
		minimum_vector = [0 for i in range(CLIQUE)]
		for idx in MC:
			minimum_vector[idx] = 1
		minimum_vectors.append(minimum_vector)	
	
	file = open("exact_solutions/"+str(problem)+".txt", "w")
	file.write(str(minimum_vectors))
	file.close()
