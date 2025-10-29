from twttr import twttr
from indoor import bankgreetig
from indoor import platecheck
from indoor import fuel
def test_bank():
    assert "$0" == bankgreetig("hello")
    assert "$100" == bankgreetig("what is your name?")
    assert "$20" == bankgreetig("how are you")


def test_vanity():
    assert "Valid" == platecheck("csd33")
    assert "Invalid" == platecheck("csd3r")
    assert "Invalid" == platecheck("23ddfd")
    assert "Valid" == platecheck("csd3")
    assert "Invalid" == platecheck("csder456")

def test_fuel():
    assert "F" == fuel("50/50")
    assert "E" == fuel("1/500")
    assert "60%" == fuel("6/10")