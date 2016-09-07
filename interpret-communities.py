# Interpretable Community Detection - https://www.github.com/franktakes/icd
#
# Goal: interpret communities and explain each community based on its composition given some node property.
# Input: nodelist file given in argv[1] with the unique node ID in column argv[1] community number in column argv[2].
#   and: nodelist file given in argv[4] with matching unique node ID in column arg[5] property to interpret with in column argv[6].
#   The header line of the input file is automatically ignored (lines 35 and 51)
# Output: for each community its id, size and a list of its composition of the form:
# attribute: percentage_of_community / percentage_of_attribute (size_of_attribute_in_community).
# Result is sorted in decreasing order of community size and per community in decreasing order of attributeś value node count.
#
# @author Frank takes@uva.nl 
#
# Requires no additional python packages.

import sys

# where the input comes from
communitiesFile = str(sys.argv[1])
communitiesIdColumn = int(sys.argv[2])
communitiesColumn = int(sys.argv[3])
interpretFile = str(sys.argv[4])
interpretIdColumn = int(sys.argv[5])
interpretColumn = int(sys.argv[6])

# helpers and counters
communityOf = {}
attributeOf = {}
nodesInCommunity = {}
communities = 0
communitySize = {}
attributeSize = {}

# read the community detection results 
with open(communitiesFile) as nodecommunities:
	killme = nodecommunities.readline() # ignore first line
	for line in nodecommunities:
		splitted = str.strip(line).split('\t')
		node = splitted[communitiesIdColumn]
		comm = splitted[communitiesColumn]
		communityOf[node] = comm
		communities = max(int(comm), int(communities))
		if int(comm) not in nodesInCommunity:
			nodesInCommunity[int(comm)] = []
			communitySize[int(comm)] = 0
		nodesInCommunity[int(comm)].append(node)
		communitySize[int(comm)] += 1
sys.stderr.write("Done reading community detection results, total of " + str(communities+1) + " communities read.\n")

# read the node property to interpret the communities with
with open(interpretFile) as nodeattributes:
	killme = nodeattributes.readline() # ignore first line
	for line in nodeattributes:
		splitted = str.strip(line).split('\t')
		node = splitted[interpretIdColumn]
		attribute = splitted[interpretColumn]
		attributeOf[node] = attribute
		if attribute not in attributeSize:
			attributeSize[attribute] = 0
		attributeSize[attribute] += 1
sys.stderr.write("Done reading node attributes.\n")

# sort communities by size
sorted_communitySize = sorted(communitySize, key=communitySize.get, reverse=True)

# determine and print community contents based on attribute
for comm in sorted_communitySize:
	nodelist = nodesInCommunity[comm]
	contents = {}	
	total = 0
	notfounderrors = 0
	for node in nodelist:
		if node in attributeOf:
			attribute = attributeOf[node]
		else:
			sys.stderr.write("attribute of node " + str(node) + " not found.\n")
			notfounderrors += 1
		if attribute not in contents:
			contents[attribute] = 0
		contents[attribute] += 1
		total += 1
		
	# sort contents of community by size
	sorted_contents = sorted(contents, key=contents.get, reverse=True)
	
	# write output
	result = [str(comm), str(total)]
	for attribute in sorted_contents:
		percentageOfCommunity = round(float(contents[attribute]*100.0) / float(total), 2)
		percentageOfattribute = round(float(contents[attribute]*100.0) / float(attributeSize[attribute]), 2)
		result.append(attribute + ": " + str(percentageOfCommunity) + "% / " + str(percentageOfattribute) + "% (" + str(contents[attribute]) + ")")
	print ("\t".join(result))

sys.stderr.write("Done writing output.\n")

