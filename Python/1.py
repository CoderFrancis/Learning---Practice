# player_name = "Axe"
# player_age = "16"
# print("The coolest guy I've ever know was " + player_name)
# print("He was only " + player_age + " but he was a well known adventurer")

# print("The Strongest \nWarrior")
# phrase = " is the Greatest Warrior"
# print(phrase.replace("Greatest", "Bravest"))

# num1 = input("Enter a number: ")
# num2 = input("Enter second number: ")
# result = int(num1) + int(num2)
# print(result)

# lucky_numbers = [4, 8, 15, 16, 23, 42]
# friends = ["Kevin", "Karen", "Jim", "Oscar", "Titan"]
# friends.insert(1, "Strong")
# print(friends)

# coordinates = (4, 5)
# print(coordinates[0])

# def say_hi(name, age):
#     print("Hello " + name + " you are " + age)

# say_hi("Titan", "18")
# say_hi("Strong", "16")

# def cube(num):
#     return num*num*num

# result = cube(3)
# print(result)

# is_Male = False
# is_Tall = False

# if is_Male and is_Tall:
#     print("You are a tall male")
# elif is_Male and not(is_Tall):
#     print("You are a short man")
# elif not(is_Male) and is_Tall:
#     print("You are not a male but are tall")
# else:
#     print("You are not a male and not tall")

# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3

# print(max_num(300, 400, 500  ))

# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#    print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invlaid operator")

# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March:",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#    "Aug": "August",
#    "Sep": "September",
#    "Oct": "October",
#    "Nov": "November",
#    "Dec": "December",
# }

# print(monthConversions["Nov"])

# i = 1
# while i <= 10:
#     i += 1
#     print(i)

# print("Finish")

# secret_word = "dog"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True

# if out_of_guesses:
#     print("You lose.")
# else:
#    print("Correct!")

# for letter in "Giraffe Academy":
#    print(letter)

# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result

# print(raise_to_power(3, 1))

# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]

# for row in number_grid:
#     for col in row:
#         print(col)

# try:
#     value = 10 / 0
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError:
#     print("Divided by zero")
# except ValueError:
#     print("Invalid input")

# example_file = open("example.txt", "r")
# for example in example_file.readlines():
#    print(example)
# print(example_file.readlines()[0])

# example_file = open("example1.txt", "w")

# example_file.write("\nBrains - AI Companion")

# example_file.close()

# from main import Student

# student1 = Student("Jim", "Business", 3.1, False)

# print(student1.name)