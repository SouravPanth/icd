# communities
Algorithms and scripts for using the Louvain community detection method as 
described in:

V.D. Blondel, J-L. Guillaume, R. Lambiotte and R. Lefebvre, 
Fast unfolding of communities in large networks, 
_Journal of Statistical Mechanics: Theory and Experiment_ 2008(10), 
P10008 (12 pages). 

This repository builds on 
[NetworkX](https://networkx.github.io) and
[python-louvain](https://bitbucket.org/taynaud/python-louvain). 

All code in this repository is scientific, meaning that little to no effort has 
been put in creating a package meeting any software engineering standards 
whatsoever. Friendly input is expected. 

## find-communities.py

This script takes as argument the filename of the edgelist of a weighted network 
and outputs a Gephi-compatible nodelist with the communities at each level of 
the algorithm. 
An optional resolution parameter can be added as a second argument. 

## dependencies

* python 2.7 or newer
* python NetworkX 1.8.1 or newer
* [python-louvain](https://bitbucket.org/taynaud/python-louvain)

