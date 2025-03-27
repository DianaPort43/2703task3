import pytest
from geometry import get_area

def test_rectangle():
    assert get_area("rectangle", width=4, height=5) == 20

def test_square():
    assert get_area("square", side=4) == 16

def test_circle():
    assert round(get_area("circle", radius=3), 2) == 28.27