# 4.5_list_copy.py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)  # ['pizza', 'falafel', 'carrot cake']

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)  # ['pizza', 'falafel', 'carrot cake', 'cannoli']
print(friend_foods)  # ['pizza', 'falafel', 'carrot cake', 'ice cream']

# Referencing is not copying / 참조는 복사가 아닙니다
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)  # ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
# ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print(friend_foods)
