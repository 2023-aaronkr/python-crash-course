# favorite_things.py
'''
This is a list.
This is a multi-line comment.
My list is my favorite things.
After input, print.
'''

favs = [] # 리스트 (배열)

# while 반복문
while(1):
    thing = input("What do you like? Enter 'q' to quit: ")

    if (thing.lower() == 'q'):
        break
    
    favs.append(thing)

# favs print
# for 반복문 = C lang: for(int i = 0; i < favs.length(); i++) { ... }
print("I like:")

for i, f in enumerate(favs):
    print(f"\t{i+1}. {f}")














