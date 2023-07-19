# 8.7_making_pizzas.py
from pizza import *  # 5
import pizza as p  # 4
from pizza import make_pizza as mp  # 3
from pizza import make_pizza  # 2
import pizza  # 1

# 1

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 2. Importing specific functions / 특정 함수를 임포트하기

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 3. Using an alias / 별칭 사용하기

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# 4. Using a module alias / 모듈에 별칭 사용하기

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 5. Importing ALL functions / 모든 함수 임포트하기

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
