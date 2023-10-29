import pytest

from dni_validator import validate_ID

def test_valid_dni():
    assert validate_ID("40923045") is True

def test_invalid_dni_short():
    assert validate_ID("12345") is False

def test_invalid_dni_long():
    assert validate_ID("123456789") is False

def test_invalid_dni_non_digit():
    assert validate_ID("abcdefg") is False

def test_invalid_dni_mixed_chars():
    assert validate_ID("1234abc") is False
