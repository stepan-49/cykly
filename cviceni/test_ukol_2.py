import pytest

from ukol_2 import pocet_sudych


def test_pocet_sudych_bezny_pripad():
    assert pocet_sudych(10) == 5


def test_pocet_sudych_bez_sudych():
    assert pocet_sudych(1) == 0


def test_pocet_sudych_liche_n():
    assert pocet_sudych(7) == 3


def test_pocet_sudych_spatny_typ():
    with pytest.raises(TypeError):
        pocet_sudych(3.5)
