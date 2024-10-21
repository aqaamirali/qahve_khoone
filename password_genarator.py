import random
letters = [
        'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I',
        'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T',
        't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '+', '^', '*']

print("welcome to password generator!")

letter_d = int(input("How Many Letters You Want In Your Password ?:\n"))
number_d = int(input("How Many Numbers You Want In Your Password ?:\n"))
Symbol_d = int(input("How Many Numbers You Want In Your Password ?:\n"))

password1 = ""
password2 = ""
password3 = ""

for number in range(number_d):
    password1 += (random.choice(numbers))

for number in range(letter_d):
    password2 += (random.choice(letters))

for number in range(Symbol_d):
    password3 += (random.choice(symbols))
# Easy level:
# print(f"{password1}{password2}{password3}")


# hard level:
password = password1 + password2 + password3
Password = ""
for n in password:
    Password += random.choice(password)
print(Password)
