# Interpret communities and explain each community based on its composition given some node property
#  Input: nodelist file given in argv[1] with the community number in column argv[2]
#    and: nodelist file given in argv[3] with the property to interpret with in column argv[4]
# Output: for each community its id, size and a list of its composition in the form
# attribute: percentage_of_community / percentage_of_attribute (size_of_attribute_in_community)
# All sorted in decreasing order of size.
# @author frank takes@uva.nl

import sys

# where the input comes from
communitiesFile = str(sys.argv[1])
communitiesColumn = int(sys.argv[2])
interpretFile = str(sys.argv[1])
interpretColumn = int(sys.argv[4])

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
		node = splitted[0]
		comm = splitted[communitiesColumn]
		communityOf[node] = comm
		communities = max(int(comm), int(communities))
		if int(comm) not in nodesInCommunity:
			nodesInCommunity[int(comm)] = []
			communitySize[int(comm)] = 0
		nodesInCommunity[int(comm)].append(node)
		communitySize[int(comm)] += 1
sys.stderr.write("Done reading community detection results, total of " + str(communities+1) + " communities read.\n")

# read the node property
with open(interpretFile) as nodeattributes:
	killme = nodeattributes.readline() # ignore first line
	for line in nodeattributes:
		splitted = str.strip(line).split('\t')
		node = splitted[0]
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
	print "\t".join(result)

sys.stderr.write("Done writing output.\n")

