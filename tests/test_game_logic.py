import pytest

# After the refactor, the game logic lives in logic_utils.py, so tests import from
# there and don't need to load Streamlit. check_guess returns (outcome, message).
from logic_utils import check_guess


# --- Tests targeting the bug we fixed: the hint direction ---
# These assert on the MESSAGE text, not just the outcome label, because the bug was
# that the outcome was correct while the hint pointed the wrong way.

def test_hint_says_go_lower_when_guess_too_high():
    # secret 10, guess 50 -> player guessed too high, so the hint must say go LOWER.
    outcome, message = check_guess(50, 10)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_hint_says_go_higher_when_guess_too_low():
    # secret 10, guess 7 -> player guessed too low, so the hint must say go HIGHER.
    outcome, message = check_guess(7, 10)
    assert outcome == "Too Low"
    assert "HIGHER" in message


@pytest.mark.parametrize(
    "guess, secret, expected_outcome, expected_word",
    [
        (60, 50, "Too High", "LOWER"),
        (40, 50, "Too Low", "HIGHER"),
        (99, 1, "Too High", "LOWER"),
        (1, 99, "Too Low", "HIGHER"),
    ],
)
def test_hint_direction_matches_outcome(guess, secret, expected_outcome, expected_word):
    outcome, message = check_guess(guess, secret)
    assert outcome == expected_outcome
    assert expected_word in message


# --- Original outcome tests (updated to the (outcome, message) return shape) ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
