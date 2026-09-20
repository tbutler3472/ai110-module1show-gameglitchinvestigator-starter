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


def test_boundary_exact_match_edge_case():
    # Exact-match wins should still work at the lowest and highest numbers in range.
    assert check_guess(1, 1) == ("Win", "🎉 Correct!")
    assert check_guess(100, 100) == ("Win", "🎉 Correct!")


def test_extreme_comparison_hint_edge_case():
    # At the far ends of the range, the direction check must remain consistent.
    assert check_guess(1, 99) == ("Too Low", "📈 Go HIGHER!")
    assert check_guess(99, 1) == ("Too High", "📉 Go LOWER!")


def test_near_boundary_guess_edge_case():
    # One-number-off guesses should still produce the correct side and hint.
    assert check_guess(99, 100) == ("Too Low", "📈 Go HIGHER!")
    assert check_guess(2, 1) == ("Too High", "📉 Go LOWER!")
