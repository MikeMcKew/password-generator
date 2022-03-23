#! python3

import string, secrets, pyperclip

def main():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for _ in range(0, 15):
        password += secrets.choice(chars)
    pyperclip.copy(password)

if __name__ == "__main__":
    main()