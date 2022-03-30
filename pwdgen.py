#! python3

import string, secrets, pyperclip

def generate_password():
    chars = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(chars) for _ in range(15))
    if (any(char.islower() for char in password) and
            any(char.isupper() for char in password) and
            any(char.isdigit() for char in password)):
        password = password.replace(password[secrets.choice(range(15))], secrets.choice(string.punctuation), 1) # replace a random char with special char
        pyperclip.copy(password)
    else:
        generate_password()

if __name__ == "__main__":
    generate_password()