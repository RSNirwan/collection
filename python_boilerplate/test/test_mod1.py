from ptut.mod1 import f

import pytest


@pytest.mark.amark
def test_f():
    assert f() == "hello world!"


def test_f2():
    assert f() == "hello world!"


def test_fixture(myfix):
    assert myfix == 20
