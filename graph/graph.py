import numpy as np 
import matplotlib.pyplot as plt

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
        e = []
        for i in range(self.vertices):
            for j in range(self.vertices):
                if j >= i: continue
                if self.edges[i,j]:
                    e.append([i,j])
        # print(e)
        return e

    def connected_components(self):
        
        is_discovered = np.zeros(self.vertices, dtype=bool)
        group         = np.empty(self.vertices, dtype=int)
        group_num     = 0
        queue         = []

        for i in range(self.vertices):

            if not is_discovered[i]:

                group[i] = group_num
                is_discovered[i] = True

                # conduct search to get all connected components to the give node
                # add all the edge nodes to the queue
                neighbors = np.arange(self.vertices)[ self.edges[i, :] == 1 ]
                queue.extend(neighbors)

                while len(queue) > 0:
                    node = queue.pop()
                    if is_discovered[node]:
                        continue
                    else:
                        is_discovered[node] = True
                        group[node] = group_num
                        
                        # add edge nodes to queue
                        new_neighbors = np.arange(self.vertices)[ self.edges[node, :] == 1 ]
                        queue.extend(new_neighbors)

                group_num += 1

        return group


    def visualize(self, kr=0.5,ks = 1, d = 1):
        # a paper on graph visualizations
        # http://jgaa.info/accepted/2003/Walshaw2003.7.3.pdf

        # positive is repusive, negative is attractive 
        # x = seperation, q = weight term
        f_repel  = lambda x,qr : (qr*kr)/(x**2) # a inverse square law for the similar to charge 
        f_spring = lambda x,qs : -qs*ks*(x - d) # a spring force with a minimum potential at separation of x = d

        # first initially distribute the points
        new_coords = 2*np.random.rand(2,self.vertices) - 1
        old_coords = 2*np.random.rand(2,self.vertices) - 1
        delta = np.sum(np.abs(old_coords - new_coords))
        counter = 1
        tol = 0.1
        

        while delta > tol:
            counter += 1
            old_coords = np.copy(new_coords)

            for i in range(self.vertices):
                for j in range(self.vertices):
                    # nudge each pair towards a minimum 
    
                    if i == j : 
                        continue 
                    
                    sep_vector = old_coords[:,i] - old_coords[:,j] # pointing from j to i (positive is repulsive)
                    sep_dist = np.sum(np.abs(sep_vector))


                    # if sep_dist == 0:
                    #     # go in a random direction
                    #     theta = 2*np.pi*np.random.rand()
                    #     rand_dir = np.array([np.cos(theta), np.sin(theta)]).reshape((2,))
                    #     # rely on the spring force for repulsion at such close distances
                    #     new_coords[:,i] +=  rand_dir * (1/counter) * f_spring(sep_dist, self.edges[i,j])

                    if sep_dist > 5:
                       # rely on the spring force for repulsion at such far distances
                        new_coords[:,i] += (sep_vector/sep_dist) * (1/counter) * f_spring(sep_dist, self.edges[i,j])

                        
                    
                    else:
                        new_coords[:,i] += (sep_vector/sep_dist) * (1/counter) * (f_repel(sep_dist,1) + f_spring(sep_dist, self.edges[i,j])) 

            # plt.scatter(new_coords[0,:],new_coords[1,:], c=['r','r','b','b'])
            # plt.show()
            delta = np.sum(np.abs(old_coords - new_coords)) # a measure of the change in the coordinates
            print(delta)

        
        coords = new_coords
        # print(coords[0,:], coords[1,:])
        return coords[0,:], coords[1,:]



        
    def __repr__(self):
        return np.array2string(self.edges)