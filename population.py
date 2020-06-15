# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 10:35:45 2020

@author: urixs
"""

import numpy as np
import random
import copy
from chromosome import Chromosome
import data_handler as dataHandler


def Population(object):
     
    def __init__(self, 
                 pop_size: int,
                 tournament_size=7,
                 mProb=.15,
                 xProb=.75,
                 verbose=1) -> None:
        
        """Population class
        Args:
            pop_size (int): Size of population
            tournament_size (int): tournament size for tournament selection
            mProb (double): mutation probability
            verbose (binary): verbosity level
        """
        self.pop_size = pop_size
        self.tournament_size = tournament_size
        self.mProb = mProb
        self.verbose=verbose
        self.n_clusters = dataHandler.get_n_clusters()
        self.n_classes = dataHandler.get_n_classes()
        self.weights = dataHandler.get_weights
        self.pop = []
        for i in range(pop_size):
            self.pop.append(Chromosome(n_clusters=self.n_clusters, 
                                       n_classes=self.n_classes,
                                       weights=self.weights))
            
        if self.verbose:
            print('Initialized population of size {}'.format(self.pop_size))
            
            
    def calc_fit_stats(self):
        """Calculation of fitness statistics"""
        
        fitness_scores = []
        for i in range(len(self.pop)):
            fitness_scores.append(self.pop[i].fitness)
            
        max_fitness = np.max(fitness_scores)
        avg_fitness = np.mean(fitness_scores)
        std_fitness = np.std(fitness_scores)
        
        if self.verbose:
            print('Max fitness: {:1.3f}, \
                  average fitness: {:1.3f}\
                  std fitness: {:1.3f}'.format(max_fitness,
                                               avg_fitness,
                                               std_fitness))
        return max_fitness, avg_fitness, std_fitness
        
            
    @staticmethod
    def find_best_fit_chromosome(pop,
                                 verbose=True):
        """Finds chromosome with best fitness"""
            
        best_fitness = -100
        best_chromosome = None
        for i in range(len(pop)):
            if pop[i].fitness > best_fitness:
                best_fitness = pop[i].fitness
                best_chromosome = pop[i]
        assert best_chromosome is not None ('Best chromosome is None')
        if verbose:
            print('Best fitness: {:1.3f}'.format(best_fitness))
        return best_chromosome
    
    
    def tournament_selection(self, 
                             preserve_best_chromosome=True):
        """Applies tournament selection, so that each element in the new \
            population is a winner of a small tournament in the current population"""
        
        new_pop = []
        
        if preserve_best_chromosome:
            winner = find_best_fit_chromosome(self.pop)
            new_pop.append(copy.deepcopy(winner))
            start_ind = 1
        else:
            start_ind = 0
            
        for i in range(start_ind, self.pop_size):
            tournament = random.sample(self.pop, self.tournament_size)
            winner = find_best_fit_chromosome(tournament)
            new_pop.append(copy.deepcopy(winner))
        
        self.pop = new_pop
    
    
    def mutate(self):
        """Applies mutation to each chromosome with probability self.mProb"""
        
        for i in range(1, self.pop_size):
            if random.random() < self.mProb:
                self.pop[i].mutate()
                
                
    def crossOver(self):
        """Applies crossOver to each two consecutive chromosomes with probability self.xProb"""

        for i in range(1, self.pop_size - 1):
            if random.random() < self.xProb:
                self.pop[i], self.pop[i + 1] = Chromosome.crossOver(self.pop[i], 
                                                                    self.pop[i + 1],
                                                                    self.n_clusters)
    

    def calc_assignment_stats(self):
        for i in range(len(self.pop)):
            self.pop[i].calc_assignment_stats()
            
    
    def evaluate_fitnesses(self):
        """Evaluates fitness of each chromosome"""
        
        for i in range(len(self.pop)):
            self.pop[i].evaluateFitness()