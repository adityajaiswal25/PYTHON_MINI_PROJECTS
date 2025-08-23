
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
import random


p = [0]*(nr_letters+nr_symbols+nr_numbers)
# print(p)
i = 0
for i in  range(0,nr_letters):
    letter = random.choice(letters)
    p[i] = letter
# print(p)
for i in range(nr_letters,nr_letters+nr_symbols):
    symbol = random.choice(symbols)
    p[i] = symbol
# print(p)
for i in range(nr_symbols+nr_letters,len(p)):
    number = random.choice(numbers)
    p[i] = number
# print(p)
pr = ""

random.shuffle(p)
for i in (p):
    pr = pr+i
print( "YOUR SAFE PASSWORD IS : ",pr)



