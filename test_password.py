import pytest, string
from password import generate_password

# Standard Functional Test
def test_password_length():
    length = 15
    password = generate_password(length)
    assert len(password) == length

def test_password_is_string():
    password = generate_password()
    assert isinstance(password, str)

def test_password_min_length():
    password = generate_password(5)
    assert len(password) >= 8

def test_password_characters():
    password = generate_password(20)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    assert has_upper and has_lower and has_digit and has_special

def test_password_uniqueness():
    passwords = {generate_password() for _ in range(100)}
    assert len(passwords) == 100