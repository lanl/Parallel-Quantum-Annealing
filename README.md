# Parallel Quantum Annealing

The Arxiv version of the paper can be found [here](https://arxiv.org/abs/2111.05995)

The classical exact solver we used to compare to D-Wave Advantage 1.1 was the fast maximum clique (fmc) solver. This solver can be downloaded [here](http://cucis.ece.northwestern.edu/projects/MAXCLIQUE/download.html)

```generate_disjoint_clique_embeddings.py``` generates all-to-all connectivity minor embeddings for different quantum annealing hardware connectivities.

```create_random_QUBOs.py``` generates test random graphs and their corresponding Maximum Clique QUBOs.

```fmc_utils.py``` are utility functions for using fmc.

```get_exact_solutions.py``` computes all maximum cliques using brute force classical clique enumeration methods in Networkx.

```run_QA.py``` Calls D-Wave in order to solve the set of test problems using both sequential and parallel QA.

```run_fmc.py``` Solves the test problems exactly using fmc, and records the time this computation used.

`hardware_edges/` contains reference connectivites for three different D-Wave QA backends.

## Authors
- [Elijah Pelofske](mailto:epelofske@lanl.gov): Information Sciences, Los Alamos National Laboratory
- [Georg Hahn](mailto:ghahn@hsph.harvard.edu): T.H. Chan School of Public Health, Harvard University
- [Hristo Djidjev](mailto:hdjidjev@msn.com): Information Sciences, Los Alamos National Laboratory and Institute of Information and Communication Technologies, Sofia, Bulgaria


## How to cite Parallel Quantum Annealing?
```latex
@misc{pelofske2021parallel,
      title={Parallel Quantum Annealing}, 
      author={Elijah Pelofske and Georg Hahn and Hristo N. Djidjev},
      year={2021},
      eprint={2111.05995},
      archivePrefix={arXiv},
      primaryClass={quant-ph}
}
```

## Copyright Notice:
© 2021. Triad National Security, LLC. All rights reserved.
This program was produced under U.S. Government contract 89233218CNA000001 for Los Alamos
National Laboratory (LANL), which is operated by Triad National Security, LLC for the U.S.
Department of Energy/National Nuclear Security Administration. All rights in the program are
reserved by Triad National Security, LLC, and the U.S. Department of Energy/National Nuclear
Security Administration. The Government is granted for itself and others acting on its behalf a
nonexclusive, paid-up, irrevocable worldwide license in this material to reproduce, prepare
derivative works, distribute copies to the public, perform publicly and display publicly, and to permit
others to do so.

**LANL C Number: C21027**

## License:
This program is open source under the BSD-3 License.
Redistribution and use in source and binary forms, with or without modification, are permitted
provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and
the following disclaimer.
 
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions
and the following disclaimer in the documentation and/or other materials provided with the
distribution.
 
3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse
or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
