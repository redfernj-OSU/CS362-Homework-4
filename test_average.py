import pytest
import average

def test_average():
    items = [100, 50]
    assert average.average(items) == 75

def test_negitive():
    items = [-50, 50]
    assert average.average(items) == 0

def test_full():
    items = []

    with pytest.raises(ValueError):
        average.average(items)
