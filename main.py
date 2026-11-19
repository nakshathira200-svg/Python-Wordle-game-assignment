from game import WordleGame


def main():
    print("\n========== WORDLE GAME ==========")

    while True:
        print("\nSelect word length:")
        print("1. Four letters")
        print("2. Five letters")
        print("3. Six letters")
        print("Q. Quit")

        choice = input("\nYour choice: ").strip().lower()

        lengths = {
            "1": 4,
            "2": 5,
            "3": 6
        }

        if choice == "q":
            print("Thanks for playing!")
            break

        if choice not in lengths:
            print("Invalid choice. Select 1, 2, 3 or Q.")
            continue

        game = WordleGame(lengths[choice])
        game.run()

        again = input("\nPlay another game? (y/n): ").strip().lower()

        if again != "y":
            print("Thanks for playing Wordle!")
            break


if __name__ == "__main__":
    main()
