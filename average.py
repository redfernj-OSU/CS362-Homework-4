import pytest


def average(items):

    if len(items) == 0:
        raise(ValueError("The list is empty."))

    temp = 0
    for x in items:
        temp += x
    return temp / len(items)

def test_average():
    items = [100, 50]
    assert average(items) == 75

def test_negitive():
    items = [-50, 50]
    assert average(items) == 0

def test_full():
    items = []

    with pytest.raises(ValueError):
        average(items)
