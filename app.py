from flask import Flask, render_template, request
import string
import random

app = Flask(__name__)

def get_lowercase_chars():
    """
    Returns a list of lowercase characters.

    Returns:
        list: A list of lowercase characters.
    """
    return list(string.ascii_lowercase)

def get_uppercase_chars():
    """
    Returns a list of uppercase characters.

    Returns:
        list: A list of uppercase characters.
    """
    return list(string.ascii_uppercase)

def get_digits():
    """
    Returns a list of digits.

    Returns:
        list: A list containing the digits 0-9.
    """
    return list(string.digits)

def get_special_characters():
    """
    Returns a list of special characters.

    This function uses the `string.punctuation` constant to generate a list of special characters.
    Special characters include punctuation marks, such as !, @, #, $, etc.

    Returns:
        list: A list of special characters.
    """
    return list(string.punctuation)

def get_random_password(has_lowercase=False, has_uppercase=False, has_digits=False, has_special_characters=False, password_length=8, can_repeat_chars=False):
    """
    Generates a random password based on the specified criteria.

    Args:
        has_lowercase (bool): Whether the password should contain lowercase characters.
        has_uppercase (bool): Whether the password should contain uppercase characters.
        has_digits (bool): Whether the password should contain digits.
        has_special_characters (bool): Whether the password should contain special characters.
        password_length (int): The length of the generated password.
        can_repeat_chars (bool): Whether characters can be repeated in the password.

    Returns:
        str: The randomly generated password.

    Raises:
        ValueError: If none of the criteria parameters (has_lowercase, has_uppercase, has_digits, has_special_characters) are set to True.
        ValueError: If there are no characters available to generate the password.
    """
    if not has_lowercase and not has_uppercase and not has_digits and not has_special_characters:
        raise ValueError("At least one of the following parameters must be True: has_lowercase, has_uppercase, has_digits, has_special_characters")
    
    characters = []
    if has_lowercase:
        characters += get_lowercase_chars()
    if has_uppercase:
        characters += get_uppercase_chars()
    if has_digits:
        characters += get_digits()
    if has_special_characters:
        characters += get_special_characters()

    if len(characters) == 0:
        raise ValueError("No characters available to generate password")

    random_password = []
    for i in range(password_length):
        c = random.choice(characters)
        random_password.append(c)
        if not can_repeat_chars:
            characters.remove(c)
        
    return ''.join(random_password)

def check_input(form_data) -> str:
    """
    Check the validity of the input form data for generating a password.

    Args:
        form_data (dict): A dictionary containing the form data.

    Returns:
        str: A string indicating the result of the input validation.

    """
    if form_data['password_length'] < 4:
        return "Password length must be at least 4 characters"
    if not form_data['has_lowercase'] and not form_data['has_uppercase'] and not form_data['has_digits'] and not form_data['has_special_characters']:
        return "At least one of the following boxes must be Checked: Include Lowercase Characters, Include Uppercase Characters, Include Number Characters, Include Special Characters"
    if not form_data['can_repeat_chars']:
        total_chars = 0
        if form_data['has_lowercase']:
            total_chars += 26   
        if form_data['has_uppercase']:
            total_chars += 26   
        if form_data['has_digits']:
            total_chars += 10
        if form_data['has_special_characters']:
            total_chars += 32
        if form_data['password_length'] > total_chars:
            return f"Not enough characters to generate a password of length {form_data['password_length']} without repeating characters, if you want to avoid repeating characters"
    return "Passed"


@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Renders the home page and generates a random password based on user input.

    Returns:
        rendered template: The rendered HTML template with the generated password and form data.
    """
    form_data = {}
    passw = None
    if request.method == 'POST':
        form_data['has_lowercase'] = bool(request.form.get('has_lowercase'))
        form_data['has_uppercase'] = bool(request.form.get('has_uppercase'))
        form_data['has_digits'] = bool(request.form.get('has_digits'))
        form_data['has_special_characters'] = bool(request.form.get('has_special_characters'))
        form_data['can_repeat_chars'] = bool(request.form.get('can_repeat_chars'))
        form_data['password_length'] = int(request.form.get('password_length'))

        if check_input(form_data) != "Passed":
            return render_template('fail.html', errormsg=check_input(form_data), form_data=form_data)
        passw = get_random_password(form_data['has_lowercase'], form_data['has_uppercase'], form_data['has_digits'], form_data['has_special_characters'], form_data['password_length'], form_data['can_repeat_chars'])    
    return render_template('home.html', passw=passw, form_data=form_data)

if __name__ == '__main__':
    app.run(debug=False)