# communities
Algorithms and scripts for using the Louvain community detection method as described in:

V.D. Blondel, J-L. Guillaume, R. Lambiotte and R. Lefebvre (2008), 
Fast unfolding of communities in large networks, 
_Journal of Statistical Mechanics: Theory and Experiment_ 2008(10), 
P10008 (12 pages). 

This repository builds on 
[NetworkX](https://networkx.github.io) and
[python-louvain](https://bitbucket.org/taynaud/python-louvain). 

All code in this repository is scientific, meaning that little to no effort has been put in creating a package meeting any software engineering standards whatsoever. 
Friendly input is expected. 


## find-communities.py
This script detects communities using the Louvain algorithm.

	python find-communities.py weighted-edgelist.csv resolution

It takes as first argument the filename of the edgelist of a weighted undirected network and outputs a Gephi-compatible nodelist with the communities at each of the K levels (iterations) of the algorithm as node attributes. 
An optional resolution parameter can be given as a second argument. 
The default value is 1, and a value lower than 1 will give more communities whereas a value higher than 1 attempts to give fewer communities. 


## interpret-communities.py
This script interprets the obtained communities by listing the composition of each community based on a node attribute. 

	python interpret-communities.py communities.csv 1 nodeattributes.csv 2

It takes 4 arguments: twice a filename and the column of that filename to use. 
It assumes that the first column (column zero) of both files is the unique identifier of the row. 
The first file specifies the communities, the second file specifies the attributes to interpret the communities with.
It then outputs the interpretation in terms of composition of the community defined by the integer in the column in the first file using the string of the column in the second file. 
All output is sorted in decreasing order by size, so the largest community is on top and the community compositions are ordered by size in decreasing order. 

## dependencies
* [python](https://www.python.org/) 2.7 or newer
* [NetworkX](https://networkx.github.io) 1.8.1 or newer
* [python-louvain](https://bitbucket.org/taynaud/python-louvain)

