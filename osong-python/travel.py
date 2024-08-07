# travel.py

# 함수 정의
def bucket_list():
    loc = {} # 전역 변수 (범위) 프로그램 모든 곳에서 사용 가능 
    active = True # 실행 플래그

    while active:
        # 지역 변수 (범위) 루프에서만 사용 가능 
        name = input("\nWhat's your name? ") 
        travel = input("Where do you want to travel? ")

        loc[name] = travel # { 'Aaron': 'Osaka' }

        repeat = input("Add another? (yes/no)")
        if repeat.lower() == 'no': # NO, No, nO, no 다 가능
            active = False

    print("\n--- Travel Bucket List ---") # Bucket List

    for name, place in loc.items():
        print(f"{name} wants to go to {place}.")

# 함수 호출하기
bucket_list() 
