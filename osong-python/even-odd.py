# even-odd.py

current_number = 0

while current_number <= 10:
    current_number += 1
    
    if current_number % 2 == 0: # 짝수 이면 나머지 문은 건너뛰기
        continue

    print(current_number) # 홀수만 출력하기
