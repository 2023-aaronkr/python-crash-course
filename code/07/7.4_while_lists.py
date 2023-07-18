# 7.4_while_lists.py
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Using remove() / remove() 사용
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)  # ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
    pets.remove('cat')

print(pets)  # ['dog', 'dog', 'goldfish', 'rabbit']
