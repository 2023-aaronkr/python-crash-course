# 9.2_my_car.py
import Car

my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modify an attribute with a method / 메서드를 통한 속성값 수정
my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

# Incrementing an attribute's value through a method / 메서드를 통한 속성값 증가
my_used_car = Car("subaru", "outback", 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
