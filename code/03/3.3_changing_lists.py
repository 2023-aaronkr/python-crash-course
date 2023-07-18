# 3.3_changing_lists.py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)  # ['trek', 'cannondale', 'redline', 'specialized']

bicycles[0] = 'giant'
print(bicycles)  # ['giant', 'cannondale', 'redline', 'specialized']

# Adding elemets / 요소 추가하기
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)  # ['trek', 'cannondale', 'redline', 'specialized']

bicycles.append('giant')
print(bicycles)  # ['trek', 'cannondale', 'redline', 'specialized', 'giant']

# Inserting elements / 요소 삽입하기
# 3.3_changing_lists.py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)  # ['trek', 'cannondale', 'redline', 'specialized']

bicycles.insert(0, 'giant')
print(bicycles)  # ['giant', 'trek', 'cannondale', 'redline', 'specialized']
