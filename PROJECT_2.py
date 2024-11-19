import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
      'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("welcome to the Password Generator!!")
n_letters = int(input("How many letters would you like in your password?"))  #4
n_numbers = int(input("How many numbers would you like in your password?"))  #3
n_symbols = int(input("How many symbols would you like in your password?"))
password = []

for i in range(n_letters):
    a = random.choice(letters)
    password += a
#print(password)

for i in range(n_numbers):
    b = random.choice(numbers)
    password += b
#print(password)

for i in range(n_symbols):
    c = random.choice(symbols)
    password += c
#print(password)  #easy level password, printed in the form of a list

#shuffling the password to increase the level
random.shuffle(password)
#print(password)  #shuffled password printed in the form of a list

pass_word = ""
for i in password:
    pass_word += i
print("your password is",pass_word)  #final shuffled password


