# list.py

kpop = [
    'TWS',
    'NCT',
    '2NE1',
    'YB',
    'New Jeans',
    'IU'
    ]

epop = [
    'One Direction',
    'Maroon 5',
    'Cold Play',
    'Beatles',
    ]

# print(kpop)
kpop.append('BTS')
kpop.insert(0, 'Jimin')
# print(kpop)

del kpop[4]
# print(kpop)

kpop.remove('Jimin')
# print(kpop)

kpop.append('binny')

kpop.sort()
# print(kpop)

for band in kpop:
    print("I like", band)
    print("I want to go to a concert!")
print("I live in Osong.")









    
