# in terminal input code hello.py = mind blown
# print("hello, world")
# in terminal input python hello.py = run program/output

# Asking user to input their name and then storing it in the name variable
# name = input("What's your name? ")

# Removes whitespace from str
# name = name.strip()

# Capitalize the user's name
# name = name.title()

# Can combine functions
# name = name.strip().title()

# To go even further
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Saying hello to user's name. Using ',' name instead '+' will automatically add a space
print(f"Hello, {first}")

# Printing out a quote
# print("Hello, \"friend\"")
