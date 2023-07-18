# 3.2_list_indexes.py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])  # trek
print(bicycles[1])  # cannondale
print(bicycles[2])  # redline
print(bicycles[3])  # specialized

print(bicycles[-1])  # specialized
print(bicycles[-2])  # redline
print(bicycles[-3])  # cannondale
print(bicycles[-4])  # trek

# Using f-strings / f-문자열 사용
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)  # My first bicycle was a Trek.
