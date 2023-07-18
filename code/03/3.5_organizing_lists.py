# 3.5_organizing_lists.py
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)  # ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()
print(cars)  # ['audi', 'bmw', 'subaru', 'toyota']

cars.sort(reverse=True)
print(cars)  # ['toyota', 'subaru', 'bmw', 'audi']

# Sorting temporarily / 일시적으로 정렬하기
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)  # ['bmw', 'audi', 'toyota', 'subaru']

print(sorted(cars))  # ['audi', 'bmw', 'subaru', 'toyota']
print(sorted(cars, reverse=True))  # ['toyota', 'subaru', 'bmw', 'audi']

print(cars)  # ['bmw', 'audi', 'toyota', 'subaru']

# Reversing / 리스트 순서 뒤집기
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)  # ['bmw', 'audi', 'toyota', 'subaru']

cars.reverse()
print(cars)  # ['subaru', 'toyota', 'audi', 'bmw']

# Length / 리스트 길이 구하기
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))  # 4
