from twttr import shorten

def test_vowels():
    assert shorten("aeiouAEIOU") == ""

def test_consonants():
    assert shorten("qwrtypsdfghjklzxcvbnm") == "qwrtypsdfghjklzxcvbnm"

def test_lower():
    assert shorten("the quick brown fox") == "th qck brwn fx"

def test_upper():
    assert shorten("TH QUICK BROWN FOX") == "TH QCK BRWN FX"

def test_number():
    assert shorten("0123456789") == "0123456789"

def test_symbol():
    assert shorten("!@#$%^&*)(_|}{:<>?.,;'][}") == "!@#$%^&*)(_|}{:<>?.,;'][}"

def test_combination():
    assert shorten("1. QUICK brown FOX!") == "1. QCK brwn FX!"