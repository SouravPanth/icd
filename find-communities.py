# Interpretable Community Detection - https://www.github.com/franktakes/icd
# 
# Goal: Find communities in a network using the Louvain algorithm.
# Input: argv[1], a (weighted) undirected network, optionally followed by argv[2], a resolution parameter.
# Output: the communities at each iteration/level of the algorithm in columns as a Gephi-compatible nodelist.
#
# @author Frank takes@uva.nl 
#
# Requires Python >= 2.7
# Requires NetworkX 1.8.1 or newer (pip install networkx) 
# Requires community module: http://perso.crans.org/aynaud/communities/index.html / https://bitbucket.org/taynaud/python-louvain
# Requires edge list input file without (e.g. Gephi's) column header line
# To remove the first line of a file, use for example: sed '1d' filename 

import networkx
import sys
import community 
import string

# set input variables
inputFile = str(sys.argv[1])
doResolution = 1. 
weighted = False
if(len(sys.argv) > 2):
	doResolution = float(sys.argv[2])		
sys.stderr.write("Using resolution " + str(doResolution) + ".\n")

# read data from edges input file 
G = networkx.Graph() # create a new undirected graph
G = networkx.read_edgelist(inputFile, nodetype=int, data=(('weight',int))) # read as int-weighted
# G = networkx.read_edgelist(inputFile, nodetype=int) # read as unweighted
sys.stderr.write("Done reading.\n")

# do community detection and get dendrograph of communities
dendo = community.generate_dendrogram(G, part_init=None, resolution=doResolution, weight='weight') 

# store communities at different levels
parts = {}
for level in range(0, len(dendo)):
	parts[level] = community.partition_at_level(dendo, level)
levels = len(dendo)

# just do plain community detection instead of nested variant
#levels = 1
#parts[0] = community.best_partition(G) # find communities

# output header to stdout
sys.stdout.write("Id")
communitySize = {}
for level in range(0, levels):
	sys.stdout.write("\tCommunity_Res" + str(doResolution) + "_Level" + str(level+1))
	communitySize[level] = -1
sys.stdout.write("\n")

# output nodelist with communities to stdout
for x in parts[0]:
	sys.stdout.write(str(x))
	for level in range(0, levels):
		sys.stdout.write("\t" + str(parts[level][x]))
		if(parts[level][x] > communitySize[level]):
			communitySize[level] = parts[level][x]
	sys.stdout.write("\n")

# some stats to stderr
sys.stderr.write("Done writing.\n")
sys.stderr.write("Communities: Level 0: n (trivial)    ")
for c in communitySize: 
	sys.stderr.write("Level " + str(c+1) + ": " + str(communitySize[c]+1) + "    ")
sys.stderr.write("\n")
sys.stderr.write("Modularity value at highest level: " + str(community.modularity(parts[levels-1], G)) + "\n")

