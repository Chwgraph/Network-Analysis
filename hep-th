# -*- coding: utf-8 -*-
"""
hep-th
"""


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpt
from matplotlib.cm import gist_rainbow_r as cmap
import random as r

H = nx.read_gml("C:/Users/17100/.spyder-py3/hep-th.gml")
data1 = H.subgraph(max(nx.connected_components(H), key=len))
n = data1.number_of_nodes()
m = data1.number_of_edges()
fig1 = plt.figure(figsize=(16, 8), dpi=100)
plt.title("Degree Distribution of Coauthorships in High-Energy Physics", fontsize=20)
degrees = [k for m, k in data1.degree]
kmin, kmax = min(degrees), max(degrees)
kRng = np.arange(kmin, kmax+1)
dh = [m/n for m in nx.degree_histogram(data1)[kmin:kmax+1]]
plt.semilogy(kRng, dh, "k.", mfc=None)
plt.xticks(np.linspace(kmin, kmax, kmax-kmin+1, True),fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("k", fontsize=20)
plt.ylabel("P(k)", fontsize=20)
plt.xlim(kmin, kmax)
plt.ylim(10**(-4),1)
print("The number of nodes in this network is:{}".format(n))
print("The number of edges in this network is:{}".format(m))

print("The average shortest distance of this network is:{}".format(nx.average_shortest_path_length(data1)))
print("The average clustering coefficient of this network is:{}".format(nx.average_clustering(data1)))

fig2 = plt.figure(figsize=(16, 8), dpi=100)
data1.graph['pos'] = nx.kamada_kawai_layout(data1)
data1.graph['degs'] = nx.degree_centrality(data1)
plt.title("Community Graph for Network of Coauthorships in High-Energy Physics", fontsize=20)
data1.graph['CNM'] = nx.community.greedy_modularity_communities(data1)
for c, community in enumerate(data1.graph['CNM']):
    for n in community: data1.nodes[n]['CNM'] = c
cNum = c+1
print("The number of communities in Network $2$ is:{}".format(cNum))

auth=[]
siz=[]
for c, community in enumerate(data1.graph['CNM']):
    siz.append(len(community))
    auth.append(sorted(community, reverse=True)[0])
print(auth[siz.index(max(siz))])


def community_network(G, algorithm):
    
    def edges_between(G, U, V):
        return sum(sum(G.has_edge(u, v) for u in U) for v in V)
    
    G_ = nx.Graph()
    for i, Q in enumerate(G.graph[algorithm]):
        intra = nx.subgraph(G, Q).number_of_edges()
        G_.add_node(i, size=len(Q), loop=intra)
    for i in G_:
        for j in range(i):
            inter = edges_between(
                G,G.graph[algorithm][i], G.graph[algorithm][j])
            if inter > 0: G_.add_edge(i, j, weight=inter)
    G_.graph['pos'] = {i: np.mean(
        [G.graph['pos'][n] for n in G.graph[algorithm][i]], axis=0) for i in G_}
    return G_


def community_diagram(G_, title, node_color):
    sizes = np.array([s for n, s in G_.nodes('size')])
    loops = np.array([l for n, l in G_.nodes('loop')])
    weights = np.array([w for u, v, w in G_.edges(data='weight')])
    
    plt.figure(figsize=(8, 4))
    plt.title(title)
    nx.draw(G_, pos=G_.graph['pos'], edgecolors='k',
            node_color=node_color,
            node_size=sizes/sizes.max()*1000,
            linewidths=loops/loops.max()*5,
            width=weights/weights.max()*5)

data1_CNM = community_network(data1, 'CNM')
community_diagram(data1_CNM,
                  'the CNM algorithm on the collaboration network',
                  [cmap(c/cNum) for c in data1_CNM])

vset = data1.nodes()


def rand_attack(H, p):
    for v in vset:
        c = [1]*int(1000*p) + [0]*int(1000*(1-p))
        d = r.choice(c)
        if d == 1:
            H.remove_node(v)
        else:
            continue

pset = np.linspace(0, 1, 100, False)
results = []
results2 = []
for p in pset:
    ssize = 0
    fremove = 0
    for i in range(100):
        W = data1.copy()
        rand_attack(W, p)
        ssize += W.subgraph(max(nx.connected_components(W), key=len, default=[])).number_of_nodes()
        fremove += 1-float(W.number_of_nodes())/data1.number_of_nodes()
    results.append((float(ssize)/n)/100)
    results2.append(float(fremove)/100)
fig3 = plt.figure(figsize=(16, 8), dpi=100)
plt.scatter(results2, results, color = "black", marker = "*")
plt.xlabel("f", fontsize=20)
plt.ylabel("S", fontsize=20)
plt.xlim(0, 1)
plt.ylim(0, 1)

h = nx.degree(data1)
T=[(d, m) for m, d in h]
degree_sequence = sorted(T, reverse=True)
T0=[m for d, m in degree_sequence]


def target_attack(W, k):
        W.remove_nodes_from(T0[:k])
        
        

results3 = []
results4 = []
for i in range(0, len(degree_sequence), 20):
    ssize = 0
    fremove = 0
    for j in range(100):
        W = data1.copy()
        target_attack(W, i)
        ssize += W.subgraph(max(nx.connected_components(W), key=len, default=[])).number_of_nodes()
        fremove += 1-float(W.number_of_nodes())/data1.number_of_nodes()
    results3.append((float(ssize)/n)/100)
    results4.append(float(fremove)/100)
print("r3:{}".format(results3))
print("r4:{}".format(results4))
fig4 = plt.figure(figsize=(16, 8), dpi=100)
plt.scatter(results3, results4, color = "black", marker = "o")
plt.xlabel("f", fontsize=20)
plt.ylabel("S", fontsize=20)
plt.xlim(0, 1)
plt.ylim(0, 1)
