# olympics.py

olympics = {}
olympics['events'] = {
    'archery': {
        'gold': 5,
        'silver': 1,
        'bronze': 1
        },
    'shooting': {
        'gold': 3,
        'silver': 2,
        'bronze': 0
        },
    'fencing': {
        'gold': 2,
        'silver': 1,
        'bronze': 0
        }
    }
ag = olympics['events']['archery']['gold']
print(f"Korea won {ag} gold medals in archery!")

"""
사전.keys() = 모든 키
사전.values() = 모든 키의 값
사전.items() = 모든 키-값 쌍
"""

for e in olympics['events'].keys():
    print(e.title())

for m in olympics['events']['archery'].values():
    print("Medal count: ", m)

print()

for key, value in olympics['events'].items():
    print(f"{key.title()}:") # key = 'archery', value = {'gold': 5, ...}

    for medal, count in value.items():
        print(f"\t{medal}: {count}")








