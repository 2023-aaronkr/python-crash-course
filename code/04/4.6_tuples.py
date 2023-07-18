# 4.6_tuples.py
dimensions = (200, 50)
print(dimensions[0])  # 200
print(dimensions[1])  # 50

# You can't change values / 값을 변경할 수 없습니다
dimensions = (200, 50)
# TypeError: 'tuple' object does not support item assignment
dimensions[0] = 250

# You can redefine the entire tuple / 튜플 전체를 재정의할 수 있습니다
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
