def evaluate(target, guess):
    if len(target) != len(guess):
        raise ValueError("Target and guess must have equal lengths.")

    result = ["gray"] * len(guess)
    remaining = {}

    # First pass: exact matches
    for i in range(len(guess)):
        if guess[i] == target[i]:
            result[i] = "green"
        else:
            remaining[target[i]] = remaining.get(target[i], 0) + 1

    # Second pass: misplaced matches
    for i in range(len(guess)):
        if result[i] == "green":
            continue

        letter = guess[i]
        if remaining.get(letter, 0) > 0:
            result[i] = "yellow"
            remaining[letter] -= 1

    return result
