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


def codebreaker(evaluation_p: tuple) -> str:
    """
    Génère une combinaison à essayer en minimisant l'espace des solutions possibles dans le pire des cas.

    Args:
        evaluation_p (tuple[int, int] | None): L'évaluation de la dernière combinaison proposée.
            Si c'est le premier essai, `evaluation_p` est `None`.

    Returns:
        str: Une combinaison à essayer, choisie pour minimiser l'espace des solutions possibles dans le pire des cas.
    """
    global possible_combinations, permanent_combinations, last_guess, dict_backtracking  # Variables globales
    
    if evaluation_p is not None:
        # Met à jour l'ensemble des combinaisons possibles en fonction de l'évaluation précédente
        common.maj_possibles(possible_combinations, last_guess, evaluation_p)
    
    best_combination = None  # Meilleure combinaison trouvée
    min_worst_case = float('inf')  # Taille minimale du pire cas

    # Parcourt toutes les combinaisons dans `permanent_combinations` pour trouver celle qui minimise le pire cas
    for test_combination in permanent_combinations:
        # Dictionnaire pour regrouper les combinaisons par résultat d'évaluation
        evaluation_groups = {}

        for comb in possible_combinations:
            # Vérifie si l'évaluation a déjà été calculée
            if (test_combination, comb) not in dict_backtracking or (comb,test_combination) not in dict_backtracking :
                # Calcule l'évaluation entre `test_combination` et `comb`
                eval_result = common.evaluation(test_combination, comb)
                dict_backtracking[(test_combination, comb)] = eval_result
                dict_backtracking[(comb,test_combination)] = eval_result
            else:
                
                # Récupère l'évaluation déjà calculée
                if (test_combination, comb) in dict_backtracking :
                    
                    eval_result = dict_backtracking[(test_combination, comb)]
                else :
                    eval_result = dict_backtracking[(comb, test_combination)]
            
            # Ajoute la combinaison au groupe correspondant à son évaluation
            if eval_result not in evaluation_groups:
                evaluation_groups[eval_result] = []
            evaluation_groups[eval_result].append(comb)
        
        # Détermine la taille du plus grand groupe d'évaluations (pire cas)
        worst_case = max(len(group) for group in evaluation_groups.values())
        
        # Si cette combinaison réduit l'espace plus que la précédente, on la choisit
        if worst_case < min_worst_case:
            best_combination = comb
            min_worst_case = worst_case

    # Sauvegarde la dernière combinaison essayée
    last_guess = best_combination
    # Retourne la meilleure combinaison trouvée
    return best_combination