# -*- coding: utf-8 -*-
import codemaker0
import random
import common  # N'utilisez pas la syntaxe "form random import XXX"
import itertools

permanent_combinations = set()
possible_combinations = set()
last_guess = None
dict_backtracking = {}

def init():
    #Initialise l'ensemble des valeurs possibles
    global possible_combinations, permanent_combinations, last_guess, dict_backtracking
    possible_combinations = set(map(''.join, itertools.product(common.COLORS, repeat = common.LENGTH)))
    permanent_combinations = possible_combinations.copy()
    last_guess = None

    dict_backtracking = {}

def codebreaker(evaluation_p):
    global possible_combinations,permanent_combinations, last_guess, dict_backtracking
    
    if evaluation_p is not None:
        # On filtre les combinaisons possibles en fonction de l'évaluation du dernier coup.
        common.maj_possibles(possible_combinations, last_guess, evaluation_p)
    
    best_combination = None
    min_worst_case = float('inf')

    # On parcourt toutes les combinaisons possibles et on choisit celle qui réduit le plus l'espace
    # des solutions dans le pire des cas.
    for test_combination in permanent_combinations:
        
        # Nous allons tester chaque combinaison meme celles qui sont impossibles
        # ET on regarde pour lequel l'ensemble de possibilité finales sera le minimum.
        evaluation_groups = {}

        for comb in possible_combinations:
            if (test_combination,comb) not in dict_backtracking :
                
                eval_result = common.evaluation(test_combination, comb)
                dict_backtracking[(test_combination,comb)]=eval_result
                
            else :
                eval_result = dict_backtracking[(test_combination,comb)]
            if eval_result not in evaluation_groups:
                evaluation_groups[eval_result] = []
            evaluation_groups[eval_result].append(comb)
        
        # Le pire des cas est la taille du plus grand groupe d'évaluations
        worst_case = max(len(group) for group in evaluation_groups.values())
        
        # Si cette combinaison réduit l'espace plus que la précédente, on la choisit.
        if worst_case < min_worst_case:
            best_combination = comb
            min_worst_case = worst_case

    last_guess = best_combination
    return best_combination
