class Graph:
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        self.m_graph = []

    def add_edge(self, node1, node2, weight):
        self.m_graph.append([node1, node2, weight])

    # Finds the root node of a subtree containing node `i`
    def find_subtree(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_subtree(parent, parent[i])

    # Connects subtrees containing nodes `x` and `y`
    def connect_subtrees(self, parent, subtree_sizes, x, y):
        xroot = self.find_subtree(parent, x)
        yroot = self.find_subtree(parent, y)
        if subtree_sizes[xroot] < subtree_sizes[yroot]:
            parent[xroot] = yroot
        elif subtree_sizes[xroot] > subtree_sizes[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            subtree_sizes[xroot] += 1

    def kruskals_mst(self):
        # Resulting tree
        result = []

        # Iterator
        i = 0
        # Number of edges in MST
        e = 0

        # Sort edges by their weight
        self.m_graph = sorted(self.m_graph, key=lambda item: item[2])

        # Auxiliary arrays
        parent = []
        subtree_sizes = []

        # Initialize `parent` and `subtree_sizes` arrays
        for node in range(self.m_num_of_nodes):
            parent.append(node)
            subtree_sizes.append(0)

        # Important property of MSTs
        # number of egdes in a MST is
        # equal to (m_num_of_nodes - 1)
        while e < (self.m_num_of_nodes - 1)and i< len(self.m_graph):
            # Pick an edge with the minimal weight
            node1, node2, weight = self.m_graph[i]
            i = i + 1
            x = self.find_subtree(parent, node1)
            y = self.find_subtree(parent, node2)
            if x != y:

                result.append([node1, node2, weight])
                self.connect_subtrees(parent, subtree_sizes, x, y)
            e = e + 1
        # Print the resulting MST
        for node1, node2, weight in result:
            print("%d - %d: %f" % (node1, node2, weight))

import numpy as np
import pandas as pd
def readFile():
    data = pd.read_csv("graph1.txt", sep="\t")
    print(data)
    data.columns=["from","to","w"]
    print(data.columns)
    adj = np.zeros((data["to"].max(),data["to"].max()),dtype=np.float32)
    print(adj.shape)
    fromList=data["from"].to_list()
    toList=data["to"].to_list()
    wList=data['w'].to_list()
    g = Graph(data["to"].max())
    for i,j,z in zip(fromList,toList,wList):
      g.add_edge(i-1,j-1,z)
      #adj[j - 1][i - 1] = z
    return g

adj= readFile()

import time
t = time.perf_counter()
adj.kruskals_mst()
print("\n*execution time :", time.perf_counter() - t)
