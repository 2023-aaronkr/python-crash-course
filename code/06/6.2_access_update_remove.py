# 6.2_access_update.py
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])  # green
print(alien_0['points'])  # 5

# Use get() to access values / get()을 사용하여 값에 액세스합니다
alien_0 = {'color': 'green', 'points': 5}

print(alien_0.get('color'))  # green
print(alien_0.get('points'))  # 5
print(alien_0.get('x_position'))  # None
# No point value assigned.
print(alien_0.get('x_position', 'No point value assigned.'))

# Update values / 값 업데이트하기
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])  # green

alien_0['color'] = 'yellow'
print(alien_0['color'])  # yellow

# Add new key-value pairs / 새 키-값 쌍 추가하기
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
alien_0['x_position'] = 0
alien_0['y_position'] = 25

# {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
print(alien_0)

# Remove key-value pairs / 키-값 쌍 제거하기
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)  # {'color': 'green', 'points': 5}

del alien_0['points']
print(alien_0)  # {'color': 'green'}
