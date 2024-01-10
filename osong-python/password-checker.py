# password-checker.py

username = 'aaron24'
password = '1234abcd'

first_name = ''
last_name = ''

print("Naver Mail Login")

uname_input = input("Username: ")
pword_input = input("Password: ")

if (username.lower() == uname_input.lower()
    and
    password.strip() == pword_input.strip()):
    print(f"Welcome to Naver Mail, {username}!")

    first_name = input("What's your first name? ")
    last_name = input("What's your last name? ")

    full_name = first_name + " " + last_name

    print(f"Nice to meet you, {full_name}!")
else:
    print(f"Incorrect login.")








    
