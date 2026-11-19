import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO

from feedback import evaluate
from game import WordleGame
from words import WORDS


class TestFeedback(unittest.TestCase):

    def test_exact_match(self):
        self.assertEqual(evaluate("crane", "crane"), ["green"] * 5)

    def test_duplicate_letters(self):
        self.assertEqual(
            evaluate("stare", "eerie"),
            ["gray", "gray", "yellow", "gray", "green"]
        )

    def test_duplicate_letters_second_case(self):
        self.assertEqual(
            evaluate("apple", "allee"),
            ["green", "yellow", "gray", "gray", "green"]
        )

    def test_absent_letters(self):
        self.assertEqual(evaluate("crane", "zzzzz"), ["gray"] * 5)

    def test_length_mismatch(self):
        with self.assertRaises(ValueError):
            evaluate("apple", "cat")


class TestGame(unittest.TestCase):

    def play(self, game, guesses):
        output = StringIO()
        with patch("builtins.input", side_effect=guesses):
            with redirect_stdout(output):
                game.run()
        return output.getvalue()

    def test_all_word_lengths(self):
        for length, target in [(4, "able"), (5, "apple"), (6, "bright")]:
            game = WordleGame(length, target=target)
            self.assertEqual(len(target), game.length)
            self.assertEqual(evaluate(target, target), ["green"] * length)

    def test_invalid_guess_does_not_consume_turn(self):
        game = WordleGame(5, target="stare")
        output = self.play(game, ["12345", "stare"])

        self.assertEqual(len(game.history), 1)
        self.assertIn("will not be counted", output)
        self.assertIn("Result: WON", output)

    def test_win_on_sixth_attempt(self):
        game = WordleGame(5, target="stare")
        guesses = ["apple", "crane", "games", "rings", "plant", "stare"]

        output = self.play(game, guesses)

        self.assertEqual(len(game.history), 6)
        self.assertIn("Result: WON", output)

    def test_loss_after_six_attempts(self):
        game = WordleGame(5, target="stare")
        guesses = ["apple", "crane", "games", "rings", "plant", "flame"]

        output = self.play(game, guesses)

        self.assertEqual(len(game.history), 6)
        self.assertIn("Result: LOST", output)

    def test_quit_game(self):
        game = WordleGame(5, target="stare")
        output = self.play(game, ["q"])

        self.assertEqual(len(game.history), 0)
        self.assertIn("Result: QUIT", output)

    def test_invalid_game_length(self):
        with self.assertRaises(ValueError):
            WordleGame(7)


if __name__ == "__main__":
    unittest.main()
