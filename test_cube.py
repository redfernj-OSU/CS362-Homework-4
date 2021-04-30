import pytest
import cube

def test_multiply():
    assert cube.volume(5, 5, 5) == 125

def test_negative():
    with pytest.raises(ValueError):
        cube.volume(-1,-1,-1)

def test_int():
    with pytest.raises(TypeError):
        cube.volume("a","b","c")
