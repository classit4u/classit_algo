# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 12:29:04 2020

@author: urixs
"""

import argparse
from population import Population

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
         pop.tournament_selection()
         pop.CrossOver()
         pop.Mutation
         pop.evaluate_fitnesses()
         pop.calc_fit_stats()
         
         print('Finished searching')



if __name__ == '__main__':
    main()