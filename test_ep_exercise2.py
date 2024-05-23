from erweiterte_programmierkonzepte.practice2 import ep_exercise2


def test_mixed():
    """
    testet gemixte wörter
    :return:
    anzahl an vokalen
    """
    assert ep_exercise2.vowels("Mein Name ist Annika"), "8 vowels."


test_mixed()


def test_no_vowels():
    """
    testet wenn kein vokale da sind
    :return:
    keine vokale vorhanden
    """
    assert ep_exercise2.vowels("qwrsdf") == 0, "no vowels."


test_no_vowels()


def test_all_vowels():
    """
    testet alle vokale
    :return:
    anzahl vokale
    """
    assert ep_exercise2.vowels("aeiouAEIOU"), "10 vowels."


test_all_vowels()


def test_numbers_symbols_ohne_vokal():
    """
    testet vokale mit zahlen und symbole
    :return:
    vokale
    """
    assert ep_exercise2.vowels("e18.09!a?"), "2 vocals."


test_numbers_symbols_ohne_vokal()


def test_empty():
    """
    testet leere strings
    :return:
    kein Inhalt
    """
    assert ep_exercise2.vowels(""), "leerer string"


test_empty()
