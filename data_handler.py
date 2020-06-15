# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 13:19:46 2020

@author: urixs
"""

from typing import List

@staticmethod
def get_weights()-> dict:
    """
    User-defined weigts for each parameter
    dict kyes should be: 'numeric' (list of floats), 
                         'categorical' (list of floats),
                         'n_pupils' (float),
                         'friends_violations' (float), 
                         'anti-friends_violations (float)' 
    """
    pass


@staticmethod
def get_n_clusters()->int:
    """
    This should return the number of clusters. 
    """
    pass


@staticmethod
def get_n_classes()->int:
    """
    This should return the number of classes. 
    """
    pass


@staticmethod
def derive_pupil_assignment_from_cluster_assignment(cluster_assignment) \
    -> List[float]:
    '''
    cluster assignment: a list of length n_cluaters, specifies the class assignment of each cluster
    pupil assignment: a list of length n_pupil, specifies the class assignment of each pupil

    This method should return pupil assignment
    '''
    pass


@staticmethod
def calc_numerical_vars_variances(pupil_assignment)-> List[float]:
    '''
    This should return a list of length n_numerical_vars, \
    of which each element is a list containing the variance of the corresponding numeric variable variances
    i.e., each grade i has variance v_ij in class j. 
    This method should return the list [var(v_11, v12...), var(v21, v22...),...]
    '''
    pass


@staticmethod
def calc_categorical_vars_variances(pupil_assignment)-> List[float]:
    '''
    This should return a list of length n_categorical_vars, \
    of which each element is a list containing the variance of the corresponding variable multinomial entropies
    i.e., for each category j of categorical i there are n_ijk pupils in class k. Let v_ij = var(nij1, nij2,...)
    This method should return the list [sum_j v1j, sum_j v2j, ...]
    '''
    pass


@staticmethod
def calc_numbers_of_pupils_in_classes(pupil_assignment)-> List[int]:
    '''
    This should return a list of length n_classes, \
    of which each element is the number of pupils in the corresponding class
    '''
    pass


@staticmethod
def calc_num_friends_violations(pupil_assignment)-> int:
    '''
    This should return the number of pupils which specified friends and were not assigned with any
    '''
    pass


@staticmethod
def calc_num_anti_friends_violations(pupil_assignment)-> int:
    '''
    This should return the number of pupils which have anti-friends and were assigned with any
    '''
    pass

    