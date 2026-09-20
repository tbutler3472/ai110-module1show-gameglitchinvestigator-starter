# FIX: Used AI assistance to make the secret number follow the selected
# difficulty range.
def get_range_for_difficulty(difficulty: str):
    """Return the inclusive secret-number range for a difficulty level.

    Args:
        difficulty: The selected difficulty name.

    Returns:
        A ``(low, high)`` tuple containing the inclusive range. Unknown
        difficulty names use the Hard range.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    """Parse raw user input into an integer guess.

    Args:
        raw: The text entered by the player.

    Returns:
        A tuple of ``(ok, guess, error_message)``. ``ok`` indicates whether
        parsing succeeded, ``guess`` contains the integer when valid, and
        ``error_message`` contains feedback when invalid.
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )

# FIX: Used AI assistance to refactor check_guess and correct the reversed
# higher/lower hints.


def check_guess(guess, secret):
    """Compare a guess with the secret and return the outcome and message.

    Args:
        guess: The player's guess.
        secret: The secret value to compare against.

    Returns:
        A tuple containing an outcome (``"Win"``, ``"Too High"``, or
        ``"Too Low"``) and the corresponding user-facing message.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update the player's score based on an outcome and attempt number.

    Args:
        current_score: The player's score before the update.
        outcome: The result of the current guess.
        attempt_number: The one-based number of the current attempt.

    Returns:
        The updated score. The current module intentionally leaves this
        operation unimplemented and raises ``NotImplementedError``.
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )
