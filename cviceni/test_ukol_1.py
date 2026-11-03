import pytest

from ukol_1 import soucet_do_n


def test_soucet_do_n_bezny_pripad():
    assert soucet_do_n(5) == 15


def test_soucet_do_n_jedna():
    assert soucet_do_n(1) == 1


def test_soucet_do_n_nula():
    assert soucet_do_n(0) == 0


def test_soucet_do_n_spatny_typ():
    with pytest.raises(TypeError):
        soucet_do_n("5")
