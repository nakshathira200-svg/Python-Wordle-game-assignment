import unittest
from feedback import evaluate
from words import WORDS


class TestWordle(unittest.TestCase):

    def test_exact_match(self):
        self.assertEqual(
            evaluate("crane", "crane"),
            ["green"] * 5
        )

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

    def test_length_mismatch(self):
        with self.assertRaises(ValueError):
            evaluate("apple", "cat")

    def test_all_word_lengths(self):
        for length in (4, 5, 6):
            matching_words = [
                word for word in WORDS if len(word) == length
            ]
            self.assertTrue(matching_words)

    def test_invalid_game_length(self):
        from game import WordleGame

        with self.assertRaises(ValueError):
            WordleGame(7)


if __name__ == "__main__":
    unittest.main()
