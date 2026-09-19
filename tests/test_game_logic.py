from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")


def test_higher_lower_hint_bug_regression():
    # Regression check for reversed comparisons: a lower guess against a high secret
    # should say "Too Low" with a "Go HIGHER!" hint, and vice versa.
    assert check_guess(4, 90) == ("Too Low", "📈 Go HIGHER!")
    assert check_guess(90, 4) == ("Too High", "📉 Go LOWER!")
