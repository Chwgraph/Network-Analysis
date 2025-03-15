# Network-Analysis
Basic network analysis for networks of American college football games and coauthorships in high-energy physics theory

# Introduction
Real-world networks are useful models for data analysis. In this project, we select two certain networks: the network of American College Football Games and the network of High-Energy Physics Theory Coauthorships as representatives. We calculated their basic parameters, detected communities in them, and performed attacks to test their network resilience. In the final section of the report, we analyze our results and determine the special network classes that they are in alternately by the properties of these two networks.

## American College Football Games
This network is a network of American football games between Division IA colleges during regular season Fall 2000. Data was provided in [1]. 

## High-Energy Physics Theory Coauthorships
This is a coauthorship network of scientists working on network theory and experiment, as compiled by M. Newman in May 2006. A figure depicting the largest component of this network can be found in the link: https://public.websites.umich.edu/~mejn/centrality/. Data was provided in [2]

Dataset for both networks can be found in the webssite: https://public.websites.umich.edu/~mejn/netdata/.

# Analysis Performed

## Basic Parameters

|Parameter|Description|
|---|---|
|Order|Number of nodes in the network|
|Size|Number of edges in the network|
|Average Shortest Distance|Average value of shortest distances between each pair of nodes|
|Average Clustering Coefficient|Average value of clustering coefficient of each node|

For detailed introduction for these concepts in graph theory and complex network theory, please refer to [3] or [4]. 

## Community Detection
Qualitatively, a community is defined as a subset of nodes within the graph such that connections between the nodes are denser than connections with the rest of nodes. This problem is relevant for social tasks (objective analysis of relationships on the web), biological inquiries (functional studies in metabolic and protein networks), or technological problems (optimization of large infrastructures). [5] Several types of algorithms exist for revealing the community structure in networks. Depending on sizes of specific local structures of networks, different algorithms are proper to use in different cases. In this project, we apply two alogrithms for the two networks alternatively.

### Girvan-Newman Algorithm
This algorithm was proposed in [1]. It detects communities by progressively removing edges from the original network. The connected components of the remaining network are the communities. Instead of trying to construct a measure that tells us which edges are the most central to communities, the Girvan–Newman algorithm focuses on edges that are most likely "between" communities. The main steps can be summarized as below:

1. The betweenness of all existing edges in the network is calculated first.
2. The edge(s) with the highest betweenness are removed.
3. The betweenness of all edges affected by the removal is recalculated.
4. Steps 2 and 3 are repeated until no edges remain.

See [1] or Wiki:https://en.wikipedia.org/wiki/Girvan%E2%80%93Newman_algorithm for detailed introductions.

### Clauset-Newman-Moore Algorithm
This algorithm was proposed in [6]. It is somehow complicated, so we would suggest you to read this paper directly for comprehending it.

# Network Resilience
We performed a random attack on the networks by randomly removing a node each time, and then calculated the number of nodes in the largest remaining component.

# References
1. Girvan, Michelle, and Mark EJ Newman. "Community structure in social and biological networks." Proceedings of the national academy of sciences 99.12 (2002): 7821-7826.
2. Newman, Mark EJ. "Finding community structure in networks using the eigenvectors of matrices." Physical Review E—Statistical, Nonlinear, and Soft Matter Physics 74.3 (2006): 036104.
3. West, Douglas Brent. Introduction to graph theory. Vol. 2. Upper Saddle River: Prentice hall, 2001.
4. Strogatz, Steven H. "Exploring complex networks." nature 410.6825 (2001): 268-276.
5. Radicchi, Filippo, et al. "Defining and identifying communities in networks." Proceedings of the national academy of sciences 101.9 (2004): 2658-2663.
6. Clauset, Aaron, Mark EJ Newman, and Cristopher Moore. "Finding community structure in very large networks." Physical Review E—Statistical, Nonlinear, and Soft Matter Physics 70.6 (2004): 066111.
