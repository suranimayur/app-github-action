from src.math_opertion import add,subtract,subtract

def test_add():
    assert add(1, 2) == 3
    assert add(6, 8) == 14
    
def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(6, 4) ==  2

