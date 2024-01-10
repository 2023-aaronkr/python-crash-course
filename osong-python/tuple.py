# tuple.py

img_dim = (1920, 1080) # HD img
print(f"img 가로: {img_dim[0]}")
print(f"img 세로: {img_dim[1]}")

insta = input("Make square for Instagram? ")

if (insta.lower() == 'y' or insta == '1' or insta == True):
    img_dim = (1080, 1080) # (1080x1080)

print(f"New img dim: ({img_dim[0]} x {img_dim[1]})")
