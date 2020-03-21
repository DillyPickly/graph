from unittest import TestCase

import graph
import numpy as np
import matplotlib.pyplot as plt

class TestInit(TestCase):
    def test(self):
        n = 5
        s = graph.Graph(n)
        self.assertEqual(s.shape, (n,n))
        self.assertEqual(s.edges.all(), 0)

class TestAddEdge(TestCase):
    def test(self):
        n = 5
        e = (2,3)
        s = graph.Graph(n)
        self.assertFalse(s.is_filled(e))
        s.add_edge(e)
        self.assertTrue(s.is_filled(e))

class TestConectedComponents(TestCase):
    def test(self):
        n = 5

        g = graph.Graph(n)
        g.add_edge((0,1))
        g.add_edge((1,2))
        g.add_edge((3,4))
        
        group = g.connected_components()
        # print(group)

        self.assertTrue(group[0] == group[1] == group[2])
        self.assertTrue(group[3] == group[4])
        self.assertFalse(group[3] == group[2])

class TestVisualize(TestCase):
    def test(self):
        n = 10

        g = graph.Graph(n)
        g.add_edge((0,1))
        g.add_edge((2,3))
        g.add_edge((3,4))

        x,y = g.visualize(0.5, 5, 0.5)
        print(len(x))
        plt.scatter(x,y)
        plt.show()

        self.assertTrue(False)
