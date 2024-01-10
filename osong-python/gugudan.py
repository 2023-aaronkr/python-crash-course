# gugudan.py

'''
for i in range(1, 10): # group
    print(f"Group {i}:")
    for j in range(1,100,10): # num
        print(f"{i} * {j} = {i*j}")
    print()
'''

from statistics import mean, median, mode

'''
digits = []
for i in range(31):
    digits.append(i)
'''
digits = [num**2 for num in range(31)]

digits.append(27**2)

print(f"Min: {min(digits)}") # 최소값 
print(f"Max: {max(digits)}") # 최대값 
print(f"Sum: {sum(digits)}") # 더하기 (결합) 
print(f"Avg: {mean(digits)}") # 평균값 
print(f"Median: {median(digits)}") # 중앙값
print(f"Mode: {mode(digits)}") # 재일 많이 있는 값 : 27 












