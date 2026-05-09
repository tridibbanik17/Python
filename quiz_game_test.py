from quiz_game import get_missed_answers
import pytest

def test_get_missed_answers():
    assert get_missed_answers([]) == "Congratulations! You got all the answers!"
    assert get_missed_answers(["A"]) == "You missed the following 1 answer: A"
    assert get_missed_answers(["A", "B"]) == "You missed the following 2 answers: A, B"