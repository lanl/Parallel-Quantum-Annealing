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
Calls fmc on a series of saved random graphs
"""
import json
import ast
import networkx as nx
import subprocess
import time
from fmc_utils import write_fmc_format, run_FMC, get_FMC_output

CLIQUE = 40

file = open("embeddings/Advantage_system1.1/clique"+str(CLIQUE)+"_embedding.json", "r")
embeddings = json.load(file)
file.close()

times = 0
for problem in range(len(embeddings)):
	file = open("random_QUBOs/graph_"+str(problem)+".txt", "r")
	G = nx.Graph(ast.literal_eval(file.read()))
	file.close()
	
	write_fmc_format(G)
	output, process_time = run_FMC()
	timing, vars, max_clique_size = get_FMC_output(output)
	times += timing
print(times)
file = open("processed_results/fmc.txt", "w")
file.write(str(times))
file.close()
