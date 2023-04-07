# Prim's Algorithm in Python
import time
import pandas as pd
import numpy as np

class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None
        self.w=None

class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d,w):
        node = AdjNode(d)
        node.next = self.graph[s]
        node.w=w
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        node.w=w
        self.graph[d] = node

def Prime():
    no_edge = 0
    selected_node[0] = True
    mst = 0
    while (no_edge < N - 1):
        minimum = I
        xa = 0
        xb = 0
        helper=0
        for m in range(N):
            if selected_node[m]:

                temp = adjList.graph[m]
                while temp:
                    if (not selected_node[temp.vertex]):
                        # not in selected and there is an edge
                        if minimum > temp.w:
                            minimum = temp.w
                            xa = m
                            xb = temp.vertex
                            helper=temp.w
                    temp=temp.next
        print(str(xa) + "->>>>" + str(xb) + "  weight:" + str(helper))
        mst += helper
        selected_node[xb] = True
        no_edge += 1
    return mst

def readFileToAdjList():
    data = pd.read_csv("graph1.txt", sep="\t")
    data.columns = ["c1", "c2", "c3"]
    g = Graph(data["c2"].max())
    for i, j, k in zip(data["c1"].to_list(), data["c2"].to_list(), data["c3"].to_list()):
        g.add_edge(i-1,j-1,k)
    return g,data["c2"].max()

adjList ,N = readFileToAdjList()
I = 9999999
# number of vertices in graph
selected_node = [0 for i in range(N)]
no_edge = 0
selected_node[0] = True
t = time.perf_counter()
mst = Prime()
print("\n*time :", time.perf_counter() - t)
print("*MST cost ", mst)
