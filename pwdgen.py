#! python3

import string, secrets, pyperclip

def main():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for _ in range(15):
        password += secrets.choice(chars)
    if (True in [char.islower() for char in password]
        and True in [char.isupper() for char in password]
        and True in [char.isdigit() for char in password]
        and True in [(char in string.punctuation) for char in password]
    ):
        pyperclip.copy(password)
    else:
        main()

if __name__ == "__main__":
    main()