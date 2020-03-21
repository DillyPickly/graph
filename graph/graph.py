import numpy as np 
import matplotlib.pyplot as plt
import time


class Graph():

    def __init__(self, n, edges = None):
        if edges is None:
            self.vertices = n
            self.edges = np.zeros((n,n),dtype=int)
            self.shape = self.edges.shape
        else :
            if edges.shape[0] is not edges.shape[1]:
                return 'Error'
            if n is not edges.shape[0]:
                return 'Error'

            self.vertices = n 
            self.edges = edges
            self.shape = edges.shape

    
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


    def visualize(self, kr = .05, ks = .08, d = 0, g = 0.5):
        # a paper on graph visualizations
        # http://jgaa.info/accepted/2003/Walshaw2003.7.3.pdf

        # positive is repusive, negative is attractive 
        # x = seperation, q = weight term
        f_repel  = lambda x,qr : (qr*kr)/(x**2) # a inverse square law for the similar to coloumb law
        f_spring = lambda x,qs : -qs*ks*(x - d) # a spring force with a minimum potential at separation of x = d
        f_gravity = lambda m : -m*g # an attractive force towards the origin
        cool = lambda t : rate*t # cooling function to slow motion

        # first initially distribute the points
        new_coords = 2*np.random.rand(2,self.vertices) - 1
        old_coords = 2*np.random.rand(2,self.vertices) - 1

        tol = .01
        converged = False
        temp = 1
        rate = 0.9
        
        while not converged:
            converged = True
        
            old_coords = np.copy(new_coords)

            for i in range(self.vertices):
                displacement = np.zeros(new_coords.shape[0]) # will update all i node

                for j in range(self.vertices):
                    # nudge each pair towards a minimum 
    
                    if i == j : continue 
                    
                    sep_vector = old_coords[:,i] - old_coords[:,j] # pointing from j to i (positive is repulsive)
                    sep_dist = np.sum(np.abs(sep_vector))
                
                    # repulsive force
                    # if sep_dist < 5:
                    displacement += (sep_vector/sep_dist) * f_repel(sep_dist,1) 
                    # print(' Repel force: ',f_repel(sep_dist,1))
                        

                    # attractive edge forces
                    displacement += (sep_vector/sep_dist) * f_spring(sep_dist, self.edges[i,j]) 
                    # print('Spring force: ',f_spring(sep_dist, self.edges[i,j]))
                    # self.edges determines if an edge connectes i and j

                displacement += (old_coords[:,i]/np.sum(np.abs(old_coords))) * f_gravity(1)

                # time.sleep(0.05)
                # print('displacement: ',displacement)
                displacement_mag = np.sum(np.abs(displacement))
                # print(displacement_mag)
                # break
                new_coords[:,i] += (displacement/displacement_mag)*min(temp, displacement_mag)
                # print(new_coords)
                # new_coords[:,i] += displacement*temp/self.vertices
                delta = np.sum(np.abs(new_coords[:,i] - old_coords[:,i]))

                print('delta: ', delta)
                # plt.scatter(new_coords[0,:],new_coords[1,:])
                # plt.show()
                if delta > tol*(ks+kr+g): converged = False

            cool(temp) 


        return new_coords[0,:], new_coords[1,:]



        
    def __repr__(self):
        return np.array2string(self.edges)