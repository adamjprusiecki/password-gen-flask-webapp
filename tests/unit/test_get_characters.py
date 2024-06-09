from app import get_lowercase_chars, get_uppercase_chars, get_digits, get_special_characters

def test_lowercase_chars():
    lowercase_list = get_lowercase_chars()
    assert all(c in "abcdefghijklmnopqrstuvwxyz" for c in lowercase_list)

def test_uppercase_chars():
    uppercase_list = get_uppercase_chars()
    assert all(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in uppercase_list)

def test_digits():
    digits_list = get_digits()
    assert all(c in "0123456789" for c in digits_list)

def test_special_characters():
    special_characters_list = get_special_characters()
    assert all(c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" for c in special_characters_list)
