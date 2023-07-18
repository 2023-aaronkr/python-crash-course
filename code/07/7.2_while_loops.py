# 7.2_while_loops.py
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Using a `quit` value / `quit` 값을 사용합니다
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# Using a flag / 플래그 사용
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
