# Find communities in a network using the Louvain algorithm and output the communities at each level of the algorithm
# Input is argv[1], a weighted undirected network and optionally argv[2] a resolution parameter
# Output the communities at each iteration of the algorithm in columns as a Gephi-compatible nodelist
# 
# @author frank takes@uva.nl
#
# Requires Python >= 2.7
# Requires NetworkX 1.8.1 or newer (pip install networkx) 
# Requires community module: http://perso.crans.org/aynaud/communities/index.html / https://bitbucket.org/taynaud/python-louvain
# Requires input file without (Gephi) column header line
# To remove the first line of a file, use for example: sed '1d' filename 

import networkx
import sys
import community 

# set input variables
inputFile = str(sys.argv[1])
doResolution = 1.
if(len(sys.argv) > 2):
	doResolution = float(sys.argv[2])

# read data from edges input file 
G = networkx.Graph() # create a new undirected graph
G = networkx.read_edgelist(inputFile, nodetype=int, data=(('weight',int))) # read as int-weighted
#G = networkx.read_edgelist(str(sys.argv[1]), nodetype=int) # read as unweighted
sys.stderr.write("Done reading.\n")

# do community detection and get dendrograph of communities
dendo = community.generate_dendrogram(G, part_init=None, weight='weight', resolution=doResolution)

# store communities at different levels
parts = {}
for level in range(0, len(dendo)):
	parts[level] = community.partition_at_level(dendo, level)
levels = len(dendo)

# just do plain community detection instead of nested
#levels = 1
#parts[0] = community.best_partition(G) # find communities

# output header
sys.stdout.write("Id")
communitySize = {}
for level in range(0, levels):
	sys.stdout.write("\tCommunity_Res" + str(doResolution) + "_Level" + str(level+1))
	communitySize[level] = -1
sys.stdout.write("\n")

# output
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

