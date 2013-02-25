'''
Created on Feb 24, 2013

@author: ney
'''
import unittest

class testGraph(unittest.TestCase):
    
    def testGraphAdd(self):
        from textProcessor.core.graphCore import Graph
        graph = Graph()
        graph.addVertex("um")
        self.assertEqual(graph.getGraph(), {'um':1}, "An error ocurred during the insertion")
        
    def testGraphCreateEdge(self):
        from textProcessor.core.graphCore import Graph
        graph = Graph()
        graph.addVertex("um")
        graph.addVertex("dois")
        graph.createEdge(nodeFrom="um", nodeTo="dois")
        
        self.assertEqual(graph.getEdges(),{("um","dois"):1}, "An error ocurred during the creation of an edge")
        
class testProcessor(unittest.TestCase):
    
    def testTokenCore(self):
        from textProcessor.core.tokenCore import Token
        
        token = Token()
        
        text = "good morning America"
        
        self.assertEqual(token.createTokens(text), ['good','morning','America'], "An error ocurred during the creation of tokens")
        
    def testGraphPopulation(self):
        from textProcessor.core.service import Service
        
        text = """ Oh, say! can you see by the dawn's early light 
                    What"""
        
        self.assertEqual(Service().populateGraph(text).getGraph(), {'Oh,': 1, 'the': 1, "dawn's": 1, 'light': 1, 'What': 1, 'early': 1, 'see': 1, 'can': 1, 'say!': 1, 'you': 1, 'by': 1}, "An error ocurred during the population of the graph")
        