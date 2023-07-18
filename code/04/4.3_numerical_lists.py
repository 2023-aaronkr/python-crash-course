# 4.3_numerical_lists.py
for value in range(5):
    print(value)

for value in range(1, 5):
    print(value)

for value in range(2, 11, 2):
    print(value)

# Statistics / 통계
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))  # 0
print(max(digits))  # 9
print(sum(digits))  # 45

# List comprehensions / 리스트 표현식
squares = [value**2 for value in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
