# 9.1_my_dog.py
import Dog

my_dog = Dog("Willie", 6)

# Accessing attributes and methods / 속성과 메서드에 접근하기
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.bark()
my_dog.sit()
my_dog.roll_over()

# Creating multiple instances / 여러 인스턴스 만들기
your_dog = Dog("Lucy", 3)

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")

your_dog.bark()
your_dog.sit()
your_dog.roll_over()
