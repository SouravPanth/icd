# Interpretable Community Detection

The two command line interface tools (scripts) in this repository help find communities in large weighted or unweighted networks and interpret the result automatically based on a node property. 
For example, for an online social network dataset, it finds communities of users and then interprets the results by for each community listing its composition based on for example the country in which the community's users live. 

Scripts use the Louvain community detection method as described in:

 > V.D. Blondel, J-L. Guillaume, R. Lambiotte and R. Lefebvre, 
Fast unfolding of communities in large networks, 
_Journal of Statistical Mechanics: Theory and Experiment_ 2008(10), 
P10008, 2008. 

This repository builds on:
 * [NetworkX](https://networkx.github.io) 
 * [python-louvain](https://bitbucket.org/taynaud/python-louvain)


## find-communities.py
This script detects communities, and works as follows:

	python find-communities.py edgelist.csv [resolution]

It takes as first argument the filename of the edgelist of a weighted (3 columns) or unweighted (2 columns) undirected network. 
The script outputs a Gephi-compatible nodelist with the communities at each of the K levels (iterations) of the algorithm as node attributes. 
An optional numeric resolution parameter can be given as a second argument. 
The default resolution is 1, where a value lower than 1 will typically give more communities whereas a value higher than 1 attempts to give fewer communities. 


## interpret-communities.py
This script interprets the obtained communities by listing the composition of each community based on a node attribute. 

	python interpret-communities.py communities.csv 0 1 nodeattributes.csv 0 2

It takes 6 arguments: 3 about the community file (1st argument) and 3 about the nodelist file (4th argument) with the attribute. 
In both cases, the first number (2nd and 5th argument) after the filename is the column number containing the unique node ID. 
The second number is the column of the community ID (3rd argument) or the column to interpret results with (6th argument). 
It then outputs the interpretation in terms of composition of the community defined by the integer in the column in the first file using the string of the column in the second file. 
All output is sorted in decreasing order by size, so the largest community is on top and the community compositions are ordered by size in decreasing order. 


## Dependencies

* [python](https://www.python.org/) 2.7 or newer
* [NetworkX](https://networkx.github.io) 1.8.1 or newer
* [python-louvain](https://bitbucket.org/taynaud/python-louvain) versions after 2016-03-24


## Disclaimer

This code was written for research-purposes only, and is and should in no way be seen as an attempt at creating a good piece of code with respect to any programming- or software-engineering standards whatsoever. 
It comes without any warranty of merchantability or suitability for a particular purpose. 
The software has exclusively been tested under the UNIX/Linux operating system, in particular Ubuntu LTS (12.04, 14.04 and 16.04) and CentOS (6.7 and 7) and Python versions 2.7 and 3.4. 

