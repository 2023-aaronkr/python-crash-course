# 2.5_combining_strings.py
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)  # ada lovelace

# Using f-strings
print(f"Hello, {full_name.title()}!")  # Hello, Ada Lovelace!

# Using format
message = "Hello, {}!".format(full_name.title())
