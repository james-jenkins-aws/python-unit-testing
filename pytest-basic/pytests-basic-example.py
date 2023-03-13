import pytest

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(1, 2) == 3
    assert calculator.add(0, 0) == 0
    assert calculator.add(-1, 1) == 0
    
def test_subtract(calculator):
    assert calculator.subtract(3, 2) == 1
    assert calculator.subtract(0, 0) == 0
    assert calculator.subtract(-1, -1) == 0