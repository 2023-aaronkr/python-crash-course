# 7.1_user_input.py
name = input("What is your name? ")
print(f"Hello, {name}!")

# Long prompt / 긴 프롬프트
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"Hello, {name}!")

# Using int() to accept numerical input / int()를 사용하여 숫자 입력 받기
age = input("How old are you? ")
age = int(age)
print(age >= 18)

# Modulo operator / 나머지 연산자
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
