# tests/test_codemaker.py
import unittest

from datas import evaluation_test

import app.mastermind.common as common


class TestCommonFunctions(unittest.TestCase):

    def test_verif_combination(self):
        """Teste la fonction verif_combination()"""
        # Cas valides
        self.assertIsNone(
            common.verif_combination("RVJB")
        )  # Longueur correcte, couleurs valides

        # Cas invalides
        self.assertEqual(
            common.verif_combination("RVJ"),
            "invalid combination : length 3 supposed to be 4",
        )  # Mauvaise longueur

        self.assertEqual(
            common.verif_combination("RVXZ"),
            "invalid combination : color X doesn't exist",
        )  # Couleur invalide

    def test_evaluation(self):
        """Test the evaluation method using the evaluation_test generated by ChatGPT -> cf datas.py"""
        for secret, guess, expected in evaluation_test:
            with self.subTest(secret=secret, guess=guess, expected=expected):
                self.assertEqual(common.evaluation(guess, secret), expected)

        # Vérifie que la fonction lève une erreur pour des tailles différentes et couleurs non présentes
        with self.assertRaises(AssertionError):
            common.evaluation("RRR", "RRRR")
            common.evaluation("RRRR", "RRR")
        with self.assertRaises(AssertionError):
            common.evaluation("RVKK", "RRRR")
            common.evaluation("RRRR", "RVKK")
        with self.assertRaises(AssertionError):
            common.evaluation("RGB", "RGBY")  # Longueurs différentes

    def test_donner_possibles(self):
        """Teste la fonction donner_possibles()"""
        tested_combination = "RVJB"
        evaluation_result = common.evaluation("RVJB", "RVBR")  # (2, 2)

        possible_combinations = common.donner_possibles(
            tested_combination, evaluation_result
        )

        # Vérifie que seules les combinaisons cohérentes avec l'évaluation restent
        for comb in possible_combinations:
            self.assertEqual(
                common.evaluation(tested_combination, comb), evaluation_result
            )

    def test_maj_possibles(self):
        """Teste la fonction maj_possibles()"""
        tested_combination = "RVJB"
        evaluation_result = common.evaluation("RVJB", "RVBR")  # (2,2)

        # Ensemble initial de combinaisons possibles
        possible_combinations = {"RVBR", "VVVV", "BBBB", "RRRR", "JBVR"}

        # Mise à jour des possibilités
        common.maj_possibles(
            possible_combinations, tested_combination, evaluation_result
        )

        # Vérifie que seules les combinaisons cohérentes restent
        for comb in possible_combinations:
            self.assertEqual(
                common.evaluation(tested_combination, comb), evaluation_result
            )


if __name__ == "__main__":
    unittest.main()
