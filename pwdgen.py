#! python3

import string, random, pyperclip

def main():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for _ in range(0, 15):
        password += random.choice(chars)
    pyperclip.copy(password)

if __name__ == "__main__":
    main()