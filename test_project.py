import pytest
from project import *

def test_convert_emojis():
    assert convert_emojis("Hi :)") == "Hi 🙂"
    assert convert_emojis("Sad :(") == "Sad 🙁"

def test_einstein_energy():
    assert einstein_energy(1) == 9e16

def test_to_float():
    assert to_float("$123") == 123.0

def test_per_to_float():
    assert per_to_float("50%") == 0.5

def test_meal_time_convert():
    assert meal_time_convert("7:30") == 7.5

def test_twttr():
    assert twttr("rabbit") == "rbbt"

def test_plate_check():
    assert plate_check("AB123") == "Valid"
    assert plate_check("123") == "Invalid"

def test_fuel_status():
    assert fuel_status("3/4") == "75%"

def test_jar():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(3)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.deposit(20)
    with pytest.raises(ValueError):
        jar.withdraw(5)

def test_is_valid_ip():
    assert is_valid_ip("192.168.0.1")
    assert not is_valid_ip("999.0.0.0")

def test_convert_hours():
    assert convert_hours("9 AM to 5 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
        convert_hours("25:00 to 26:00")

def test_emojize_text():
    assert emojize_text(":smile:")=="😄"
    assert emojize_text("the :moon: is very beutiful") =="the 🌔 is very beutiful"
