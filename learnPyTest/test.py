import pytest
from main import count_vowels

@pytest.mark.parametrize("string, expected", [
    ("", 0),
    ("аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU", 30),
    ("dkptRRRвждлМФ", 0),
    ("Эх, взъярюсь, толкну флегматика, дай же щец горячих, Пётр", 16),
    ("AaAaAa", 6),
])

def test_count_vowels(string, expected):
    assert count_vowels(string) == expected
