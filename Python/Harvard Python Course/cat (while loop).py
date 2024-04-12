i = 0
while i < 3:
    print("meow")
    i += 1

# or
# i = 3
# while i != 0
#   print("meow")]
# i = i - 1

# also
for _ in range(3):
    print("dog")

# continuing
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

# improvement
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


def meow(n):
    print