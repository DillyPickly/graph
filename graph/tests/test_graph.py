from unittest import TestCase

import graph
import numpy as np

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

# class()

