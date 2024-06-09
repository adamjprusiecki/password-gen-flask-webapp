from app import check_input

def test_check_input_password_length():
    form_data = {'password_length': 3, 'has_lowercase': True, 'has_uppercase': False, 'has_digits': False, 'has_special_characters': False, 'can_repeat_chars': False}
    assert check_input(form_data) == "Password length must be at least 4 characters"

def test_check_input_no_criteria_set():
    form_data = {'password_length': 8, 'has_lowercase': False, 'has_uppercase': False, 'has_digits': False, 'has_special_characters': False, 'can_repeat_chars': False}
    assert check_input(form_data) == "At least one of the following boxes must be Checked: Include Lowercase Characters, Include Uppercase Characters, Include Number Characters, Include Special Characters"

def test_check_input_no_repeating_chars_lowercase_fail():
    form_data = {'password_length': 27, 'has_lowercase': True, 'has_uppercase': False, 'has_digits': False, 'has_special_characters': False, 'can_repeat_chars': False}
    assert check_input(form_data) == f"Not enough characters to generate a password of length {form_data['password_length']} without repeating characters, if you want to avoid repeating characters"

def test_check_input_no_repeating_chars_lowercase_pass():
    form_data = {'password_length': 26, 'has_lowercase': True, 'has_uppercase': False, 'has_digits': False, 'has_special_characters': False, 'can_repeat_chars': False}
    assert check_input(form_data) == "Passed"

def test_check_input_no_repeating_chars_lowercase_uppercase_fail():
    form_data = {'password_length': 53, 'has_lowercase': True, 'has_uppercase': True, 'has_digits': False, 'has_special_characters': False, 'can_repeat_chars': False}
    assert check_input(form_data) == f"Not enough characters to generate a password of length {form_data['password_length']} without repeating characters, if you want to avoid repeating characters"

def test_check_input_no_repeating_chars_lowercase_uppercase_pass():
    form_data = {'password_length': 52, 'has_lowercase': True, 'has_uppercase': True, 'has_digits': False, 'has_special_characters': False, 'can_repeat_chars': False}
    assert check_input(form_data) == "Passed"

def test_check_input_no_repeating_chars_lowercase_uppercase_digits_fail():
    form_data = {'password_length': 63, 'has_lowercase': True, 'has_uppercase': True, 'has_digits': True, 'has_special_characters': False, 'can_repeat_chars': False}
    assert check_input(form_data) == f"Not enough characters to generate a password of length {form_data['password_length']} without repeating characters, if you want to avoid repeating characters"

def test_check_input_no_repeating_chars_lowercase_uppercase_digits_pass():
    form_data = {'password_length': 62, 'has_lowercase': True, 'has_uppercase': True, 'has_digits': True, 'has_special_characters': False, 'can_repeat_chars': False}
    assert check_input(form_data) == "Passed"

def test_check_input_no_repeating_chars_lowercase_uppercase_digits_special_fail():
    form_data = {'password_length': 95, 'has_lowercase': True, 'has_uppercase': True, 'has_digits': True, 'has_special_characters': True, 'can_repeat_chars': False}
    assert check_input(form_data) == f"Not enough characters to generate a password of length {form_data['password_length']} without repeating characters, if you want to avoid repeating characters"

def test_check_input_no_repeating_chars_lowercase_uppercase_digits_special_pass():
    form_data = {'password_length': 94, 'has_lowercase': True, 'has_uppercase': True, 'has_digits': True, 'has_special_characters': True, 'can_repeat_chars': False}
    assert check_input(form_data) == "Passed"