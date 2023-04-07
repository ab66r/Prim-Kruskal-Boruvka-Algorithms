'''
Judafa Saleem Alharabi 442004186    Group:4
code refrences: 
https://www.geeksforgeeks.org/boruvkas-algorithm-greedy-algo-9/

'''

import numpy as np
import pandas as pd
import time


# Graph Class (to represent the graph) 
class Graph:

    def __init__(self, ver):
        self.numV = ver  # number of vertices
        self.graph = []  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function (uses path compression technique) to find the shortest bath
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A function to union of set of x and set of y
    # (union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y)

        #finde smaller rank tree and put it under the higher rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        # if the two trees had the same rank 
        else:
            parent[yroot] = xroot  #let one be the root and increse it by 1
            rank[xroot] += 1

    # kruskal's algorithm to find the MST
    def boruvkaMST(self):
        parent = []
        rank = []

        # array to store index of the subset cheapest edge 
        cheap = []

        #trees is the number of trees witch is also the number of vertices
        trees = self.numV
        MSTtree = 0  # the final tree that is represent the MST 

        # ti create subsets of the vertices with single elements (each tree root)
        for node in range(self.numV):
            parent.append(node)
            rank.append(0)
            cheap = [-1] * self.numV

       
        #loop to combine the pervios trees
        while trees > 1:
            # go through all edges and update cheap each time(finding the  cheapist edge and add it each time)
            for i in range(len(self.graph)):
                u, v, w = self.graph[i]
                set1 = self.find(parent, u)
                set2 = self.find(parent, v)

                #if the eadges dosent belong to the same set check cheap for each edges of set1 and set2 
                if set1 != set2:

                    if cheap[set1] == -1 or cheap[set1][2] > w:
                        cheap[set1] = [u, v, w]

                    if cheap[set2] == -1 or cheap[set2][2] > w:
                        cheap[set2] = [u, v, w]

            
            # add the cheapest edges to MST tree
            for node in range(self.numV):
                # check if cheap dose exists for the current set 
                if cheap[node] != -1:
                    u, v, w = cheap[node]
                    set1 = self.find(parent, u)
                    set2 = self.find(parent, v)

                    if set1 != set2:
                        MSTtree += w
                        self.union(parent, rank, set1, set2)
                        #print the eages that are incloded in the MST tree
                        print("Edge %d-%d with weight %f included in MST" % (u, v, w))
            trees = trees - 1

            # reset cheapest array
            cheap = [-1] * self.numV

        print("Weight of MST is %f" % MSTtree)


def readFile():
    data = pd.read_csv("graph1.txt", sep="\t") #to read the data into a (DataFrame)
    print(data)
    data.columns=["from","to","w"] #spesfie the data columns index
    print("data.columns:",data.columns)
    adj = np.zeros((data["to"].max(),data["to"].max()),dtype=np.float32) #to create a zero elements array with float data type 
    print(adj.shape)
    fromList=data["from"].to_list() #to read the data into list used (to to_list() method to convert pandas obj to python list)
    toList=data["to"].to_list()
    wList=data['w'].to_list()
    for i,j,z in zip(fromList,toList,wList):
      adj[i-1][j-1]=z
      adj[j - 1][i - 1] = z
    return  adj

adj= readFile()
g = Graph(len(adj))
for i in range(len(adj)):
    for j in range(len(adj)):
        if adj[i][j]!=0:
            g.addEdge(i,j,adj[i][j])
t = time.perf_counter()
g.boruvkaMST()
print("execution time :", time.perf_counter() - t)

