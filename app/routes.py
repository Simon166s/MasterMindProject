from flask import Blueprint, render_template, request, url_for, session
from app.mastermind import *


color_dic = {
    'R': 'red',          # Rouge
    'B': 'blue',         # Bleu
    'V': 'green',        # Vert
    'J': 'yellow',       # Jaune
    'O': 'orange',       # Orange
    'N': 'black',
    'M': 'brown',
    'G': 'grey'

}


# Création d'un blueprint
main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
def index():
    

    # La fonction index() sera appelée quand l'utilisateur visite la racine ("/")
    return render_template("index.html")



@main.route("/human_player", methods=['GET', 'POST'])
def human_player():
    """
    Adaptation du jeu sans utiliser play, avec comptage des essais
    """
    # Initialisation
    if request.method == 'GET':
        codemaker0.init()  # Appel de init() seulement lors de la première visite
        session['codemaker_initialized'] = True  # Marquer que l'initialisation a été faite
        
    solution = codemaker0.solution
    message = ""
    win_message = ""
    combination = ""
    lenght = common.LENGTH
    colors_name = [color_dic[code] for code in common.COLORS]
    colors = ", ".join(common.COLORS)
    cplaced = None
    iplaced = None

    # On récupère le nombre d'essais dans la session (s'il existe)
    if 'nbr_of_try' not in session:
        session['nbr_of_try'] = 0  # Initialiser le nombre d'essais si inexistant

    # Récupérer le nombre d'essais actuel
    nbr_of_try = session['nbr_of_try']

    if request.method == "POST":
        combination = request.form.get('combination', '').upper()
        erreur = human_codebreaker.verif_combination(combination)

        # Si l'utilisateur a fait une erreur dans la combinaison
        if erreur:
            message = erreur
        else:
            message = f"Combination accepted: {combination}"

            # Évaluation de la combinaison
            cplaced, iplaced = common.evaluation(combination, codemaker0.solution)

            # Si la combinaison est correcte, affichage du message de victoire
            if cplaced >= common.LENGTH:
                win_message = f"Bravo ! Trouvé {combination} en {nbr_of_try} essais"
                session.pop('nbr_of_try')  # On réinitialise les essais une fois le jeu gagné
            else:
                # Sinon, incrémenter le nombre d'essais
                session['nbr_of_try'] = nbr_of_try + 1

    # Retourner le template avec les variables nécessaires
    return render_template(
        "human_player.html", 
        combination=combination, 
        message=message, 
        lenght=lenght, 
        colors=colors, 
        cplaced=cplaced, 
        iplaced=iplaced, 
        colors_name=colors_name, 
        win_message=win_message, 
        nbr_of_try=nbr_of_try,
        solution = solution
    )
