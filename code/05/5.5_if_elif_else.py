# 5.5_if_elif_else.py
# IF statement / IF 문
age = 12

if age >= 18:
    print("You are old enough to vote!")

# ELIF statement / ELIF 문
if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 10
else:
    ticket_price = 15

print(f"Your ticket costs ${ticket_price}.")

# ELSE statement / ELSE 문
if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 10
elif age < 65:
    ticket_price = 15
else:
    ticket_price = 10

print(f"Your ticket costs ${ticket_price}.")

if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 10
elif age < 65:
    ticket_price = 15

print(f"Your ticket costs ${ticket_price}.")
