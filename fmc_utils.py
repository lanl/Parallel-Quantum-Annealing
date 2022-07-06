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
Calls compiled fmc in order to exactly find the Maximum Clique of an input graph G
"""

import ast
import networkx as nx
import subprocess
import time

def write_fmc_format(G):
	file = open("graph.mtx", "w")
	file.write("%%MatrixMarket matrix coordinate pattern symmetric\n")
	file.write(str(len(G))+" "+str(len(G))+" "+str(len(list(G.edges())))+"\n")
	for e in list(G.edges()):
		if e[0] < e[1]:
			file.write(str(e[1]+1)+" "+str(e[0]+1)+"\n")
		else:
			file.write(str(e[0]+1)+" "+str(e[1]+1)+"\n")
	file.close()
def run_FMC():
	start = time.process_time()
	out = subprocess.run(["./fmc", "-t", "0", "-p", "graph.mtx"], capture_output=True)
	end = time.process_time()
	tmp = out.stdout
	string = tmp.decode("utf-8")
	return string, end-start
def get_FMC_output(input):
	chunks = input.splitlines()
	for chunk in chunks:
		if "Time taken : " in chunk:
			time_with_sec = chunk.replace("Time taken : ", "")
			timing = float(time_with_sec.replace("SEC", ""))
		if "Maximum clique: " in chunk:
			max_clique_vars = chunk.replace("Maximum clique: ", "")
			splits = max_clique_vars.split(" ")
			vars = []
			for s in splits:
				if s != "":
					vars.append(int(s)-1)
		if "Max clique Size : " in chunk:
			max_clique_size = int(chunk.replace("Max clique Size : ", ""))
	return timing, vars, max_clique_size
