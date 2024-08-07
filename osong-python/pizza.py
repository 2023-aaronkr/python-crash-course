# pizza.py

import random as r 

loc = "Domino's"

# 제목 출력하기
msg = "|======================|"
msg += "\n| Welcome to " + loc + "! |"
msg += "\n|======================|"
print(msg)

# 주문하기
my_toppings = []
have_toppings = [
    'pepperoni', 'ham', 'potato',
    'extra cheese', 'cheddar cheese',
    'mushrooms', 'onions', 'pineapple'
    ]

# 사용자 입력 받기
while(1): # True
    topping = input("What topping do you want? 'Q' to quit: ")

    if topping.lower() == 'q':
        break

    my_toppings.append(topping)

# 주문 확인하기
print("You ordered: ")

for i, topping in enumerate(my_toppings):
    print(f"{i+1}. {topping.title()}")

    # 토핑 있는지 확인
    if topping in have_toppings:
        print(f"Adding {topping}.")
    else:
        print(f"Sorry, no {topping}.")

# 배달 시간 알려주기
time = r.randint(15, 40)
print(f"Order delivery in {time} mins!")












