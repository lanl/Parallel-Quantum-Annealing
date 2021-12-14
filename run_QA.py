"""
Calls the D-Wave backend using both sequential and parallel QA
The inputs are some random set of graphs of size CLIQUE
The results are written to Json files
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

CLIQUE = 40#Size of the problems to be embedded on the chip
N_DWAVE_CALLS = 100

def get_qubit_list(embedding):
        out = []
        for a in embedding:
                out += embedding[a]
        return out
def Start_DWave_connection():
    client = Client.from_config()
    solver_name = client.default_solver
    DWave_solver = client.get_solver("Advantage_system1.1")
    A = DWave_solver.undirected_edges
    connectivity_graph = nx.Graph(list(A))
    return connectivity_graph, DWave_solver

Target, solver = Start_DWave_connection()

# D-Wave parameters
params = {"num_reads": 1000, "annealing_time": 20, "programming_thermalization": 0, "readout_thermalization": 0}

file = open("embeddings/Advantage_system1.1/clique"+str(CLIQUE)+"_embedding.json", "r")
embeddings = json.load(file)
file.close()

non_parallel_results = {}

combined_QUBOs = {}
bqm_tracking = {}

### Sequential QA
for problem in range(len(embeddings)):
	file = open("random_QUBOs/"+str(problem)+".txt", "r")
	QUBO = ast.literal_eval(file.read())
	file.close()
	qubit_list = get_qubit_list(embeddings[problem])
	embedding_dict_json = embeddings[problem]
	embedding_dict = {}
	for i in embedding_dict_json:
		embedding_dict[int(i)] = embedding_dict_json[i]
	physical_subgraph = Target.subgraph(qubit_list)
	bqm = dimod.BinaryQuadraticModel.from_qubo(QUBO)
	bqm_tracking[problem] = bqm
	chain_strength_fixed = embedding.chain_strength.uniform_torque_compensation(bqm, prefactor=UTC)#Uniform Torque Compensation chain strength calculation
	embedded_qubo = embedding.embed_qubo(QUBO, embedding_dict, physical_subgraph, chain_strength=chain_strength_fixed)
	combined_QUBOs = {**combined_QUBOs, **embedded_qubo}
	all_vectors = []
	all_QPU = 0
	all_energies = []
	for rep_solve in range(N_DWAVE_CALLS):
		while (True):
			try:
				sampleset = solver.sample_qubo(embedded_qubo, answer_mode='raw', **params)
				vectors = sampleset.samples
				energies = sampleset.energies
				break
			except:
				print("fail", flush=True)#Connection problem
				time.sleep(1)
				continue
		QPU_time = sampleset['timing']['qpu_access_time']/float(1000000)#Timing is given in microseconds
		all_QPU += QPU_time
		all_vectors += vectors
		all_energies += energies
	non_parallel_results[problem] = [all_QPU, all_vectors, all_energies]
file_name = str(programming_thermalization)+"_"+str(readout_thermalization)+"_"+str(AT)+"_"+str(UTC)
file = open("DWave_results/non_parallel_"+file_name+".json", "w")
json.dump(non_parallel_results, file)
file.close()


### Parallel QA
all_vectors = []
all_QPU = 0
all_energies = []
for rep_solve in range(N_DWAVE_CALLS):
	while (True):
		try:
			sampleset = solver.sample_qubo(combined_QUBOs, answer_mode='raw', **params)
			vectors = sampleset.samples
			energies = sampleset.energies
			break
		except:
			print("fail", flush=True)
			time.sleep(1)
			continue
	QPU_time = sampleset['timing']['qpu_access_time']/float(1000000)
	all_QPU += QPU_time
	all_vectors += vectors
	all_energies += energies
	parallel_results["QPU_time"] = all_QPU
file_name = str(programming_thermalization)+"_"+str(readout_thermalization)+"_"+str(AT)+"_"+str(UTC)
file = open("DWave_results/parallel_"+file_name+".json", "w")
json.dump([all_QPU, all_vectors, all_energies], file)
file.close()
