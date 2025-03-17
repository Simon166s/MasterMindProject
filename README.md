# Mastermind - Interface Graphique avec Flask

Ce projet implémente une interface graphique pour le jeu Mastermind en utilisant Flask.

## 🛠 Installation

1. **Cloner le dépôt**
   ```sh
   git clone <URL_DU_DEPOT>
   cd <NOM_DU_DEPOT>
   ```

2. **Créer et activer un environnement virtuel** (recommandé) :
   ```sh
   python -m venv venv
   source venv/bin/activate  # Sur macOS/Linux
   venv\Scripts\activate     # Sur Windows
   ```

3. **Installer les dépendances** :
   ```sh
   pip install -r requirements.txt
   ```

## 🚀 Lancer l'interface graphique

1. Exécuter le script principal :
   ```sh
   python run.py
   ```

2. Ouvrir le lien affiché dans le terminal (généralement `http://127.0.0.1:5000`).

## 📦 Structure du projet

Le projet utilise Flask, et le dossier `mastermind` est un **package Python**. Ainsi, pour exécuter des fichiers internes, il faut utiliser la commande suivante :
```sh
python -m app.mastermind.[nomdufichiersansextension]
```



