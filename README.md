This is a simple script to generate random passwords. Intended for Windows; functionality on other OSes is not guaranteed.

For easy use, create a batch file to run the script:

1. Pull the repo to local
2. Install requirements.txt (pip install -r requirements.txt)
    - It is recommended to first create a virtual environment to install requirements.txt into (python -m venv <venv-name>)
    - If you create a virtual environment, activate it with .\\\<venv-name>\scripts\activate (cd to correct directory)
3. Create pwdgen.bat file in a folder that is included in PATH
4. In pwdgen.bat, add the path to Python and the path to pwdgen.py separated by a space (C:\path\to\python.exe C:\path\to\pygen.py)
    - If you created a virtual environment, the path to python.exe should be .\\\<venv-name>\scripts\python.exe (copy full path to python.exe)
5. Press Windows+R, type "pwdgen", click OK
6. You should now have a randomly generated password on your clipboard, ready for convenient pasting!

Passwords are 15 characters long and can include the following characters:

abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~