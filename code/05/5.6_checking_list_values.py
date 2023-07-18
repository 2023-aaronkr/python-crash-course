# 5.6_checking_list_values.py
favorite_foods = ['pizza', 'ice cream', 'chocolate', 'chicken', 'beef']

if favorite_foods:
    print("You have favorite foods!")

# Check empty lists / 빈 목록 확인하기
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# Check for a value in a list / 목록에 값이 있는지 확인하기
requested_toppings = ['mushrooms', 'onions', 'pineapple']

if 'green peppers' in requested_toppings:
    print("Adding green peppers.")

if 'green peppers' not in requested_toppings:
    print("No green peppers.")
