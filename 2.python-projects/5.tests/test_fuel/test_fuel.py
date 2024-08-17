from fuel import convert, gauge
from pytest import raises

def test_full():
    assert convert("99/100") == 99
    assert gauge(99) == "F"

    assert convert("1/1") == 100
    assert gauge(100) == "F"

def test_empty():
    assert convert("1/99") == 1
    assert gauge(1) == "E"

    assert convert("0/99") == 0
    assert gauge(0) == "E"

def test_fractional():
    assert convert("3/4") == 75
    assert gauge(75) == "75%"

    assert convert("2/4") == 50
    assert gauge(50) == "50%"

    assert convert("1/4") == 25
    assert gauge(25) == "25%"

def test_error():

    with raises(ValueError):
        convert("2/1")

    with raises(ZeroDivisionError):
        convert("1/0")

    