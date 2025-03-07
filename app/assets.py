import os
from flask_assets import Environment, Bundle

def compile_assets(app):
    """Configure and compile SCSS files into CSS."""
    assets = Environment(app)

    # Définir les chemins en fonction de la structure du projet
    scss_dir = os.path.join(app.root_path, 'static', 'scss')
    css_output_path = os.path.join(app.root_path, 'static', 'css')

    # Vérifier que le dossier CSS existe, sinon le créer
    if not os.path.exists(css_output_path):
        os.makedirs(css_output_path)

    # Vérifier que les fichiers SCSS existent
    scss_files = ['style.scss', 'human_player.scss']
    for scss_file in scss_files:
        scss_path = os.path.join(scss_dir, scss_file)
        if not os.path.exists(scss_path):
            raise FileNotFoundError(f"Le fichier SCSS est introuvable : {scss_path}")

    # Configuration du bundle SCSS -> CSS
    scss_bundle = Bundle(
        'scss/style.scss', 
        filters='libsass', 
        output='css/style.css'  # Générer un fichier style.css pour style.scss
    )
    human_player_bundle = Bundle(
        'scss/human_player.scss', 
        filters='libsass', 
        output='css/human_player.css'  # Générer un fichier human_player.css pour human_player.scss
    )
    
    assets.register('scss_all', scss_bundle)
    assets.register('human_player_css', human_player_bundle)
    
    # Compiler les SCSS en CSS
    scss_bundle.build()
    human_player_bundle.build()
