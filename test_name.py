import pytest
import name

def test_full_name():
    assert name.full_name("Jacob", "Redfern") == "Jacob Redfern"

def test_no_last_name():
    with pytest.raises(TypeError):
        name.full_name("Jacob")

def test_num_name():
    with pytest.raises(TypeError):
        name.full_name(0,1)
