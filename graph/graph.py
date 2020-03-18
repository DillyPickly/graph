import numpy as np 

class Graph():

    def __init__(self, n):
        self.vertices = n
        self.edges = np.zeros((n,n),dtype=int)
        self.shape = self.edges.shape
    
    def add_edge(self,edge):
        ### add an edge via a tuple
        self.edges[edge[0], edge[1]] = 1
        self.edges[edge[1], edge[0]] = 1

    def is_filled(self, edge):
        ## check edge via tuple coords
        return self.edges[edge]

    def get_edges(self):
        return self.edges

    # def connected_component(self, vertex):
        


    def __repr__(self):
        return np.array2string(self.edges)