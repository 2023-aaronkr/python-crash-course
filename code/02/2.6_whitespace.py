# 2.6_whitespace.py

# Adding whitespace / 공백 추가하기
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Strippign whitespace / 공백 제거하기
favorite_language = 'python   '
print(favorite_language.rstrip())  # python

favorite_language = '   python'
print(favorite_language.lstrip())  # python

favorite_language = '   python   '
print(favorite_language.strip())  # python
