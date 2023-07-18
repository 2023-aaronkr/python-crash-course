# 6.3_dictionary_looping.py
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# Loop through keys / 키를 반복합니다
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key in user_0.keys():
    print(key.title())

# Access a value with the key name / 키 이름으로 값을 액세스합니다
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# Loop through values / 값 반복하기
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for value in user_0.values():
    print(value.title())
