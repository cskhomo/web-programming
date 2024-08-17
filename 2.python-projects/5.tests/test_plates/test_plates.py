from plates import is_valid

def test_length():
    assert is_valid("ZN") == True
    assert is_valid("VANITY") == True
    assert is_valid("Z") == False
    assert is_valid("VANITIES") == False

def test_start():
    assert is_valid("1ZN") == False
    assert is_valid("100") == False

def test_symbols():
    assert is_valid("ZN!") == False
    assert is_valid("Z N") == False

def test_numbers():
    assert is_valid("ZN10") == True
    assert is_valid("VA10NI") == False
    assert is_valid("ZN01") == False
