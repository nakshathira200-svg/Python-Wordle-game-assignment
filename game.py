import random
from words import WORDS
from feedback import evaluate


class WordleGame:
    MAX_ATTEMPTS = 6

    def __init__(self, length=5, target=None):
        if length not in (4, 5, 6):
            raise ValueError("Word length must be 4, 5, or 6.")

        available_words = [
            word for word in WORDS if len(word) == length
        ]

        self.length = length
        self.target = target if target is not None else random.choice(available_words)

        if self.target not in available_words:
            raise ValueError("Target must be in the word list for this length.")

        self.history = []

    def display_history(self):
        if not self.history:
            return

        print("\nGuess History:")
        for number, (guess, feedback) in enumerate(self.history, start=1):
            print(f"{number}. {guess.upper()} -> {' '.join(feedback)}")

    def display_summary(self, status):
        print("\n========== GAME SUMMARY ==========")
        print(f"Result: {status}")
        print(f"Target word: {self.target.upper()}")
        print(f"Guesses used: {len(self.history)}/{self.MAX_ATTEMPTS}")
        print("==================================")

        self.display_history()

    def run(self):
        print(f"\nWORDLE - {self.length} LETTERS")
        print(f"You have {self.MAX_ATTEMPTS} valid guesses.")
        print("Enter Q to quit.\n")

        while len(self.history) < self.MAX_ATTEMPTS:
            guess = input(
                f"Guess {len(self.history) + 1}/{self.MAX_ATTEMPTS}: "
            ).strip().lower()

            if guess == "q":
                print("\nGame abandoned.")
                self.display_summary("QUIT")
                return

            if (
                len(guess) != self.length
                or not guess.isalpha()
                or not guess.isascii()
            ):
                print(f"Invalid input! Enter exactly {self.length} letters.")
                print("This attempt will not be counted.\n")
                continue

            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))

            print("Feedback:", " | ".join(feedback))
            self.display_history()

            if guess == self.target:
                print("\nCongratulations! You guessed the word!")
                self.display_summary("WON")
                return

        print("\nGame over! You have used all six guesses.")
        self.display_summary("LOST")
