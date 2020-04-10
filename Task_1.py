# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:30:46 2020

@author: Dima & Sagi
"""

import pandas as pd
import numpy as np

class graph:
    
    def __init__(self):
        
        self.source_to_dest_dict = {}
        self.dest_to_source_dict = {}
        self.page_rank = {}
        
        
    def load_graph(self, path):
        """
        The function loads the csv file(graph)
        :param path: path of the csv file
        :return: None
        """
        df = pd.read_csv(path, names=['source', 'dest'])
        self.source_to_dest_dict = df.applymap(str).groupby('source')['dest'].apply(list).to_dict()  # src points to dest
        self.dest_to_source_dict = df.applymap(str).groupby('dest')['source'].apply(list).to_dict()  #dest who are pointing at the source
        
    def calculate_page_rank(self, beta=0.85, epsilon=0.001, maxIterations=20):
        """
        Calculates the PageRank for each of the nodes in the graph.
        The calculation will end in one of two stop conditions:
        after maxIterations iterations, or when the difference
        between two iterations is smaller than δ.
        
        :param beta:
        :param epsilon:
        :param maxIterations: 
        :return: None
        """
        
    
    def get_PageRank(self, node_name):
        """
        Returns the PageRank of a specific node.
        Return “-1” for non-existing name
        :param node_name: The node name
        :return: The PageRank of the given node name 
        :rtype: double
        """
        
    def get_top_PageRank(self, n):
        """
        Returns a list of n nodes with the highest PageRank value.
        The list should be ordered according to the PageRank values from high to low
        :params n: How many nodes.
        :return: List of pairs:<node name, PageRank value >
        :rtype: list.
        """
    
    def get_all_PageRank(self):
        """
        Returns a list of the PageRank for all the nodes in the graph
        The list should include pairs of node id, PageRank value of that node.
        The list should be ordered according to the PageRank values from high to low
        :params: None
        :return: List of pairs:<node name, PageRank value >
        """    
        
    def calcuate_CC(self):
        """
        Calculates the (undirected) clustering coefficient of each of the nodes in the graph
        :param: None
        :return: None
        """
    
    def get_CC(self, node_name):
        """
        Returns the clustering coefficient of a specific node.
        Return “-1” for non-existing name
        :param node_name: The node name
        :type node_name: String
        :return: The CC of the given node name
        :rtype: Double
        """
        
    def get_top_CC(self, n):
        """
        Returns a list of n nodes with the highest clustering coefficients.
        The list should be ordered according to the CC values from high to low.
        :param n: How many nodes
        :return: List of pairs:<node name, CC value >
        """
        
    def get_all_CC(self):
        """
        Returns a list of the clustering coefficients for all the nodes in the graph
        The list should include pairs of node id, CC value of that node.
        The list should be ordered according to the CC values from high to low.
        :param: None
        :return: List of pairs:<node name, CC value >
        """
    
    
    def get_average_CC(self):
        """
        Returns a simple average over all the clustering coefficients values 
        :param: None
        :return: average CC
        """
        
