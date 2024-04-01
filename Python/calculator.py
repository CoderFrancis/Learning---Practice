# int function can be used to change str to int
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x + y)

# 'z:,' adds in a comma to the calculation
# print(f"{z:,}")

x = float(input("What's x? "))
y = float(input("What's y? "))

# the ', 2' rounds the solution to the two decimal points
z = round(x / y, 2)

# or 
z = x / y

print(f"{z:.2f}")

# print(z)
