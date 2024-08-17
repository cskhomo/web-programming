from bank import value

def test_win():
    assert value("What's up") == 100

def test_lose_upper():
    assert value("HELLO") == 0

def test_lose_lower():
    assert value("hello") == 0

def test_draw_upper():
    assert value("HEY") == 20

def test_draw_upper():
    assert value("hey") == 20