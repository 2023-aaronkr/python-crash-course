# 4.2_list_indentation.py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

# Indentation errors / 들여쓰기 오류
magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# print(magician) # IndentationError: expected an indented block

# message = "Hello Python world!"
#     print(message) # IndentationError: unexpected indent

# Logical errors / 논리적 오류
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("Thank you, everyone. That was a great magic show!")

# Forgetting the colon / 콜론을 잊어버린 경우
magicians = ['alice', 'david', 'carolina']
# for magician in magicians # SyntaxError: invalid syntax
#   print(magician)
