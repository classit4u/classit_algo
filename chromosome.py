# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 10:35:45 2020

@author: urixs
"""
import random
import numpy as np
import data_handler as dataHandler

def Chromosome(object):
    
    def __init__(self, 
                 n_clusters,
                 n_classes,
                 weights,
                 cluster_assigment = None):
        
        self.fitness = -100
        self.n_clusters = n_clusters
        self.n_classes = n_classes
        self.weights = weights
        if cluster_assigment is None:
            self.cluster_assigment = []
            for i in range(self.n_clusters):
                self.cluster_assigment.append(random.randint(0, self.n_classes - 1))
    
        else: 
            self.cluster_assigment = cluster_assigment
    
    def mutate(self):
        """
        Replaces the class of a random custer by a random class
        """
        index = random.randint(0, self.n_clusters)
        new_class = random.randint(0, self.n_classes)
        self.cluster_assigment[index] = new_class
        
   
    @staticmethod
    def crossOver(c1, c2, n_clusters):
        """

        Parameters
        ----------
        c1 : Chromosome
            father chromosome.
        c2 : Chromosome
            mother Chromosome

        Returns
        -------
        c1_new : Chromosome
            1st child chromosome
        c2_new : Chromosome
            12t child chromosome
            
        Selects a random intersection point, and crosses the parents    

        """
        intersect_idx = random.randint(n_clusters)
        c1_new_assignment = c1[:intersect_idx] + c2[intersect_idx:]
        c2_new_assignment = c2[:intersect_idx] + c1[intersect_idx:]
        c1_new = Chromosome(n_clusters=c1.n_clusters,
                            n_classes=c1.n_classes,
                            weights=c1.weights,
                            cluster_assigment=c1_new_assignment)
        c2_new = Chromosome(n_clusters=c1.n_clusters,
                            n_classes=c1.n_classes,
                            weights=c1.weights,
                            cluster_assigment=c2_new_assignment)
        
        return c1_new, c2_new    
    
    
    def evaluateFitness(self):
        """
        Evaluates the fitness of the chromosome, 
        by multiplying the statustics with the correponding weights and summing

        Returns
        -------
        None.

        """
        
        # get weights
        numeric_weights = np.array(self.weights['numeric'])
        categorical_weights = np.array(self.weights['categorical'])
        n_pupils_weight = self.weights['n_pupils']
        friends_violations_weight = self.weights['friends_violation']
        anti_friends_violations_weight = self.weights['anti-friends_violation']
        
        long_assignment = dataHandler.derive_pupil_assignment_from_cluster_assignment(self.cluster_assignment)
        numeric_variances = dataHandler.calc_numerical_vars_variances(long_assignment)
        categorical_variances = dataHandler.calc_categorical_vars_variances(long_assignment)
        n_pupils_var = np.var(dataHandler.calc_numbers_of_pupils_in_classes(long_assignment))
        friends_violations = dataHandler.calc_num_friends_violations(long_assignment)
        anti_friends_violations = dataHandler.calc_num_anti_friends_violations(long_assignment)
        
        numeric_penalty = np.sum(numeric_weights * numeric_variances)
        categorical_penalty = np.sum(categorical_weights * categorical_variances)
        n_pupil_penalty = n_pupils_weight * n_pupils_var
        friends_violations_penalty = friends_violations_weight * friends_violations
        anti_friends_penalty = anti_friends_violations_weight * anti_friends_violations
        
        total_penalty = numeric_penalty + \
                        categorical_penalty + \
                        n_pupil_penalty + \
                        friends_violations_penalty + \
                        anti_friends_penalty    
                        
        self.fitness = 1. / total_penalty
        