import pytest
import string
from app import get_random_password

def test_password_length():
    password = get_random_password(has_lowercase=True,password_length=10)
    assert len(password) == 10

def test_has_lowercase():
    password = get_random_password(has_lowercase=True)
    assert any(c.islower() for c in password)

def test_has_uppercase():
    password = get_random_password(has_uppercase=True)
    assert any(c.isupper() for c in password)

def test_has_digits():
    password = get_random_password(has_digits=True)
    assert any(c.isdigit() for c in password)

def test_has_special_characters():
    password = get_random_password(has_special_characters=True)
    assert any(c in string.punctuation for c in password)

def test_can_repeat_chars():
    password = get_random_password(has_lowercase=True,can_repeat_chars=True,password_length=1000)
    assert len(set(password)) < len(password)

def test_no_criteria_set():
    with pytest.raises(ValueError):
        get_random_password()

def test_no_characters_available():
    with pytest.raises(ValueError):
        get_random_password(has_lowercase=False, has_uppercase=False, has_digits=False, has_special_characters=False)