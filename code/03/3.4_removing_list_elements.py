# 3.4_removing_list_elements.py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)  # ['trek', 'cannondale', 'redline', 'specialized']

del bicycles[0]
print(bicycles)  # ['cannondale', 'redline', 'specialized']

# pop()
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)  # ['trek', 'cannondale', 'redline', 'specialized']

popped_bicycle = bicycles.pop()
print(bicycles)  # ['trek', 'cannondale', 'redline']
print(popped_bicycle)  # specialized

popped_bicycle = bicycles.pop(1)
print(bicycles)  # ['trek', 'redline', 'specialized']
print(popped_bicycle)  # cannondale

# remove()
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)  # ['trek', 'cannondale', 'redline', 'specialized']

bicycles.remove('cannondale')
print(bicycles)  # ['trek', 'redline', 'specialized']
