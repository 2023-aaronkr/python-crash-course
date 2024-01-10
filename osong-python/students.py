# students.py
'''
Collecting student info in a dictionary.
1. Name
2. Hobbies
3. Fave Food
4. Height
'''

students = {
    1101: {
        'name': '고현우',
        'height': 172,
        'food': '김치찌개',
        'hobbies': ['games', 'soccer', 'movies']
        },
    1125: {
        'name': '이광훈',
        'height': 170,
        'food': '스시',
        'hobbies': ['games', 'sleep', 'movies']
        },
    1127: {
        'name': '임하송',
        'height': 176,
        'food': '삼겹살',
        'hobbies': ['games', 'boxing', 'drama']
        },
    1521: {
        'name': '이희성',
        'height': 165,
        'food': '삼겹살',
        'hobbies': ['basketball', 'YouTube', 'movies']
        },
    1822: {
        'name': '이준',
        'height': 180,
        'food': '치킨',
        'hobbies': ['coding', 'basketball', 'movies']
        },
    2024: {
        'name': '에런',
        'height': 180,
        'food': '한우',
        'hobbies': ['coding', 'biking', 'reading']
        },
    }

# dictionary = { key: value } # item
'''
for s in students: # 키
    print(s)

for s in students.keys(): # 키
    print(s)

for s in students.items(): # item
    print(s)
'''

for s in students.values(): # 값
    print(f"{s['name']}'s height is {s['height']}.")

# Sports
sports = ['soccer', 'baseball', 'basketball', 'tennis', 'boxing']

msg = "These students like sports: "

for s in students.values():
    for h in s['hobbies']:
        if h in sports:
            msg += s['name'] + ", "

print(msg)













    





