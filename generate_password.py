#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many lower letters would you like in your password?\n"))
nr_upper= int(input("How many upper letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_list = []
for l in range(0,nr_letters):
    letter = random.choice(letters)
    password_list +=letter
for u in range(0,nr_upper):
    uppers = random.choice(upper)
    password_list+=uppers
for s in range(0,nr_symbols):
    symbol = random.choice(symbols)
    password_list+=symbol
for n in range(0,nr_numbers):
    number = random.choice(numbers)
    password_list+=number

random.shuffle(password_list)
password = ''.join(password_list)
print(password)