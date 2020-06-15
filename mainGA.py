# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 12:29:04 2020

@author: urixs
"""

import argparse
from population import Population
import data_handler as dataHandler

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--save_dir",
                    type=str,
                    default='./saved_class-assignments',
                    help="Directory for assignments")
parser.add_argument("--mProb",
                    type=float,
                    default=0.15,
                    help="Mutation probability")
parser.add_argument("--xProb",
                    type=float,
                    default=0.7,
                    help="CrossOver probability")
parser.add_argument("--popSize",
                    type=int,
                    default=100,
                    help="Population size")
parser.add_argument("--tournamentSize",
                    type=int,
                    default=7,
                    help="Tournament size")
parser.add_argument("--nGenerations",
                    type=int,
                    default=70000,
                    help="Numnber of generations")
parser.add_argument("--verbose",
                    type=int,
                    default=1,
                    help="Verbosity level")
parser.add_argument("--print_every",
                    type=int,
                    default=1,
                    help="Print statistics to console every this number of generations")
args = parser.parse_args(args=[])


def main():
        
     pop = Population(popSize=args.popSize,
                      mProb=args.mProb,
                      xProb=args.xProb,
                      tournament_size=args.tournamentSize,
                      verbose=args.verbose)
     
     pop.calc_fit_stats()
     
     # main loop
     for i in range(args.nGenerations):
         print('Generation {}'.format(i))
         # apply genetic steps
         pop.tournament_selection()
         pop.CrossOver()
         pop.Mutation
         pop.evaluate_fitnesses()
         
         # print statistics to console
         if i % args.print_every == 0:
             max_fitness, avg_fitness, std_fitness = pop.calc_fit_stats()
             best = pop.find_best_fit_chromosome
             best_cluster_assignment = best.cluster_assignment
             best_pupil_assignment = \
                 dataHandler.derive_pupil_assignment_from_cluster_assignment(best_cluster_assignment)
             num_pupils = dataHandler.calc_numbers_of_pupils_in_classes(best_pupil_assignment)
             friends_violations = dataHandler.calc_num_friends_violations(best_pupil_assignment)
             anti_friends_violations = dataHandler.calc_num_anti_friends_violations(best_pupil_assignment)
             print('Generation {}/{}, Avg fitmess: {:1.3f}({:1.3f})), best fitness: {:1.3f}, \
                   num pupils: {} \
                   friends violations: {}, anti-friends violations: {}'\
                       .format(i, 
                               args.nGenerations, 
                               avg_fitness,
                               std_fitness,
                               max_fitness,
                               num_pupils,
                               friends_violations,
                               anti_friends_violations    
                               ))
         
     print('Finished searching')
     best = pop.find_best_fit_chromosome
     best_cluster_assignment = best.cluster_assignment
     best_pupil_assignment = \
        dataHandler.derive_pupil_assignment_from_cluster_assignment(best_cluster_assignment)
     # best_pupil_assignment contains the search result
     


if __name__ == '__main__':
    main()