#!/usr/bin/env python3
import importlib
import common
import past_evaluations

# TO DO : passer les commentaires en anglais 
def get_codebreaker_module(version: int):
    """Importe dynamiquement le module codebreaker de la version donnée."""
    try:
        return importlib.import_module(f"codebreaker{version}")
    except ImportError:
        raise ValueError(f"Module codebreaker{version} non trouvé.")

def get_codemaker_module(version: int):
    """Importe dynamiquement le module codemaker de la version donnée."""
    try:
        return importlib.import_module(f"codemaker{version}")
    except ImportError:
        raise ValueError(f"Module codemaker{version} non trouvé.")

def check_compatibility(codemaker_version: int, codebreaker_version: int):
    """
    Vérifie que le couple codemaker/codebreaker est compatible.
    On lève une erreur si l'on tente de jouer codemaker0 avec codebreaker2,
    car codebreaker2 a besoin d'une évaluation complète.
    """
    if codemaker_version == 0 and codebreaker_version == 2:
        raise ValueError("Incompatibilité détectée : codebreaker2 nécessite une évaluation complète et ne peut pas être utilisé avec codemaker0.")

def play(codemaker_version: int, codebreaker_version: int, reset_solution = True, quiet = False) -> int:
    """
    Joue une partie pour un codebreaker donné sur une solution déjà initialisée ou pas dans le module codemaker.
    Le codebreaker est cependant réinitialisé pour chaque partie.
    """
    check_compatibility(codemaker_version, codebreaker_version)
    codemaker_module, codebreaker_module = get_codemaker_module(codemaker_version), get_codebreaker_module(codebreaker_version)

    # Permet de pouvoir comparer deux codebreaker sur la meme solution
    if reset_solution:
        codemaker_module.init()

    codebreaker_module.init()  # Réinitialisation du codebreaker
    ev = None
    nbr_of_try = 0

    if not quiet:
        print('combinations de taille {}, couleurs disponibles {}'.format(common.LENGTH, common.COLORS))
    while True:
        combination = codebreaker_module.codebreaker(ev)
        ev = codemaker_module.codemaker(combination)
        nbr_of_try += 1
        if not quiet:
            print("Essai {} : {} ({},{})".format(nbr_of_try, combination, ev[0], ev[1]))
        if ev[0] >= common.LENGTH:
            if not quiet:
                print("Bravo ! Trouvé {} en {} essais".format(combination, nbr_of_try))
            return nbr_of_try

def play_log(codemaker_version: int, codebreaker_version: int, reset_solution = True, quiet = False) -> int:
    
    """
    Joue une partie pour un codebreaker donné sur la solution déjà initialisée dans le module codemaker.
    Le codebreaker est réinitialisé pour chaque partie, tandis que le codemaker conserve la solution.
    """
    check_compatibility(codemaker_version, codebreaker_version)
    codemaker_module, codebreaker_module = get_codemaker_module(codemaker_version), get_codebreaker_module(codebreaker_version)

    
    # Permet de pouvoir comparer deux codebreaker sur la meme solution
    if reset_solution:
        codemaker_module.init()
    codebreaker_module.init()  # Réinitialisation du codebreaker
    ev = None
    nbr_of_try = 0 
        ##### Seule chose qui change du programme play
    with open("log.txt", 'w') as log:
        if not quiet:
            print('combinations de taille {}, couleurs disponibles {}'.format(common.LENGTH, common.COLORS))
        while True:
            combination = codebreaker_module.codebreaker(ev)
            ev = codemaker_module.codemaker(combination)
            nbr_of_try += 1
            log.write(combination + "\n")
            log.write(f"{ev[0]},{ev[1]} \n")
            if not quiet:
                print("Essai {} : {} ({},{})".format(nbr_of_try, combination, ev[0], ev[1]))
            if ev[0] >= common.LENGTH:
                if not quiet:
                    print("Bravo ! Trouvé {} en {} essais".format(combination, nbr_of_try))
                return nbr_of_try

play_log(2, 3)