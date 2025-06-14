import unittest

import app.mastermind.codemaker2 as codemaker2
import app.mastermind.common as common
import app.mastermind.past_evaluations as past_evaluations

# To do créer un jeu de test en entré dont on connais la sortie


class TestCodemaker2(unittest.TestCase):

    def setUp(self):
        """
        Initialise les variables globales avant chaque test.
        """
        codemaker2.solution = "RRRR"
        codemaker2.possible_combinations = {
            "RRRR",
            "VVBB",
            "VBBR",
            "BBVV",
            "VRBB",
            "VVVV",
        }
        codemaker2.permanent_combinations = codemaker2.possible_combinations.copy()
        past_evaluations.dict_backtracking = {}

    def test_exact_match(self):
        """
        Teste si une combinaison identique à la solution donne (4,0).
        """
        result = codemaker2.codemaker("RRRR")
        self.assertEqual(
            result, (4, 0), "Erreur: la combinaison exacte ne retourne pas (4,0)"
        )

    def test_partial_match(self):
        """
        Teste si une combinaison avec 2 couleurs bien placées retourne (2,0).
        """
        result = codemaker2.codemaker("VVRR")
        self.assertEqual(
            result, (2, 0), "Erreur: la combinaison partielle ne retourne pas (2,0)"
        )

    def test_no_match(self):
        """
        Teste si une combinaison sans correspondance retourne (0,0).
        """
        result = codemaker2.codemaker("BBBB")
        self.assertEqual(
            result,
            (0, 0),
            "Erreur: la combinaison sans correspondance ne retourne pas (0,0)",
        )

    def test_solution_update_difficulty(self):
        """
        Vérifie que la solution mise à jour est la plus difficile à deviner.
        """
        codemaker2.codemaker("VVRR")

        # La nouvelle solution doit appartenir à l'ensemble des solutions possibles
        self.assertIn(
            codemaker2.solution,
            codemaker2.possible_combinations,
            "Erreur: la solution mise à jour n'est pas dans les possibilités.",
        )
        # La nouvelle solution doit etre la plus dure a trouver, parmis les possible combination, elle doit etre dans le groupe avec le plus d'ambiguité donc dans {RRRR, VVBB, VBBR, VVVV}
        self.assertIn(
            codemaker2.solution,
            {"RRRR", "VVBB", "VBBR", "VVVV"},
            "Erreur: la solution mise à jour n'est pas optimisée pour maximiser la difficulté.",
        )

    def test_evaluation_storage(self):
        """
        Vérifie que les évaluations sont stockées pour éviter des recalculs.
        """
        codemaker2.codemaker("VVVV")
        self.assertIn(
            ("VVVV", "RRRR"),
            past_evaluations.dict_backtracking,
            "Erreur: l'évaluation n'a pas été enregistrée.",
        )
        self.assertIn(
            ("RRRR", "VVVV"),
            past_evaluations.dict_backtracking,
            "Erreur: l'évaluation inverse n'a pas été enregistrée.",
        )


if __name__ == "__main__":
    unittest.main()
