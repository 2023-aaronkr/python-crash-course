# pizza.py

import random as r

msg = 'Welcome to Mr. Pizza!'
msg += '====================='
print(msg)

my_toppings = [] # 리스트
available_toppings = [
    'mushrooms', 'olives', 'green peppers',
    'pepperoni', 'pineapple', 'cheese',
    'sausage', 'onions', 'hamburger'
    ]

# Take Order
while(1):
    topping = input('What toppings do you want? \'Q\' to quit: ')

    if topping.lower() == 'q':
        break

    my_toppings.append(topping)

# Repeat Order
print("You want: ")

for i, t in enumerate(my_toppings):
    print(f"{i+1}. {t.title()}")
    
    if t in available_toppings:
        print(f"Adding {t}.")
    else:
        print(f"Sorry, no {t}.")

min = r.randint(20,40)
print(f"Order delivery in {min}min.")
    
    







