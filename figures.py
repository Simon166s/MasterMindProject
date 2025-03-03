import codemaker0
import common
import matplotlib.pyplot as plt

#TO DO: réfléchir au mieux entre diagramme de dispersion et histogramme pour la fonction show gain 

NUMBER_OF_GAME = 100

def get_number_of_try(codebreaker_version: int) -> int:
    nbr_of_try = 0
    maker_evaluation = None

    # Construit le nom du module à importer (par ex. "codebreaker0", "codebreaker1", etc.)
    module_name = f"codebreaker{codebreaker_version}"
    try:
        # Import du module en fonciton de la méthode choisie 
        codebreaker_module = __import__(module_name)
    except ImportError:
        raise ValueError(f"Module {module_name} non trouvé.")
    
    codebreaker_module.init() # on initialise le codebreaker afin de vider le set des combinaisons testées à la partie d'avant
    while maker_evaluation != common.LENGTH:
        nbr_of_try += 1
        # On appelle la fonction codebreaker de la version importée en passant l'évaluation précédente
        proposition = codebreaker_module.codebreaker(maker_evaluation)
        # codemaker0.codemaker renvoie un tuple : on récupère le premier élément (la valeur d'évaluation)
        maker_evaluation = codemaker0.codemaker(proposition)[0]
        
    return nbr_of_try

def show_histrogramme(version: int):
    resultats = []
    for _ in range(NUMBER_OF_GAME):
        codemaker0.init() # on doit tester sur une nouvelle partie à chaque fois donc il faut reinitialiser la solution
        resultats.append(get_number_of_try(version))
    plt.hist(resultats, bins=range(min(resultats), max(resultats) + 2), align='left', edgecolor='orange')
    plt.xlabel('Valeurs retournées')
    plt.ylabel('Fréquence')
    plt.title(f'Histogramme du nombre de partie nécessaire pour trouver la solution sur {NUMBER_OF_GAME} parties jouées')
    plt.show()


def get_gain(version1 : int, version2 : int)-> int:
    return get_number_of_try(version1) - get_number_of_try(version2)


def show_gain(version1: int, version2: int):
    gains = []
    for _ in range(NUMBER_OF_GAME):
        codemaker0.init() # on doit tester sur une nouvelle partie à chaque fois donc il faut reinitialiser la solution
        gains.append(get_gain(version1, version2))
    # Création d'un diagramme de dispersion
    parties = list(range(1, NUMBER_OF_GAME + 1))
    plt.scatter(parties, gains, color='orange')
    plt.xlabel('Numéro de partie')
    plt.ylabel('Gain')
    plt.title(f'Diagramme de dispersion du gain entre codebreaker{version1} et codebreaker{version2} sur {NUMBER_OF_GAME} parties')
    print("gains:", gains)
    plt.show()

show_gain(0,1)