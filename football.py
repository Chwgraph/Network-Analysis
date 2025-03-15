# -*- coding: utf-8 -*-
"""
football
"""


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpt
from matplotlib.cm import gist_rainbow_r as cmap

data1 = nx.read_gml(r"C:\Users\17100\.spyder-py3\football.gml")
n = data1.number_of_nodes()
m = data1.number_of_edges()
fig1 = plt.figure(figsize=(16, 8), dpi=100)
plt.title("Degree Distribution of Network of American College Football Matches", fontsize=20)
degrees = [k for m, k in data1.degree]
kmin, kmax = min(degrees), max(degrees)
kRng = np.arange(kmin, kmax+1)
dh = [m/n for m in nx.degree_histogram(data1)[kmin:kmax+1]]
plt.plot(kRng, dh, "r.--", mfc=None)
plt.xticks(np.linspace(kmin, kmax, kmax-kmin+1, True), fontsize=30)
plt.yticks(np.linspace(0, 1, 6, True), fontsize=20)
plt.xlabel("k", fontsize=20)
plt.ylabel("P(k)", fontsize=20)
plt.xlim(kmin, kmax)
plt.ylim(0, 1)
print("The number of nodes in this network is:{}".format(n))
print("The number of edges in this network is:{}".format(m))

print("The average shortest distance of this network is:{}".format(nx.average_shortest_path_length(data1)))
print("The average clustering coefficient of this network is:{}".format(nx.average_clustering(data1)))

data1.graph['GN'] = list(nx.community.girvan_newman(data1))[::-1]
fig2 = plt.figure(figsize=(16, 8), dpi=100)

for it in data1.graph['GN'][-10]:
    print(len(list(it)))

def modularity(G, partitions):
    Qs = partitions
    E = G.number_of_edges()
    B = nx.modularity_matrix(G)
    C = np.array([[1 if i in Q else 0 for Q in Qs] for i in G])
    return np.trace(C.T@B@C) / (2*E)

plt.axhline(0, c='k', ls='--', lw=1)

M = {len(Qs): modularity(data1, Qs) for Qs in data1.graph['GN']}
M[1] = modularity(data1, (set(data1),))
plt.plot(M.keys(), M.values(), 'ko-', mfc='w', lw=1)

plt.xlabel('number of partitions', fontsize=20)
plt.ylabel('modularity $M$', fontsize=20)
plt.title('Girvan-Newman Algorithm on the American College Football Games\n', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()

data1.graph['pos'] = nx.kamada_kawai_layout(data1)
data1.graph['degs'] = nx.degree_centrality(data1)
for c, community in enumerate(data1.graph['GN'][-10]):
    for n in community: data1.nodes[n]['GN'] = c
cNum = c+1


def data1_plot(title, node_color):
    plt.figure(figsize=(9, 6))
    plt.title(title)
    nx.draw(data1, pos=data1.graph['pos'],
            width=.25, edgecolors='k', linewidths=.75,
            node_size=[k*1000 for k in data1.graph['degs'].values()],
            node_color=node_color)

data1_plot('the Girvan-Newman algorithm on the American College Football Games Network',
                [cmap(c/cNum) for n, c in data1.nodes('GN')])
