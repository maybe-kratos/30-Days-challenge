import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
no_letters= 4
no_symbols = 3
no_numbers = 2

password = ""
for i in range (1,no_letters+1):
    p = random.choice(letters)
    password = password+p
for i in range (1,no_symbols+1):
    p = random.choice(symbols)
    password = password+p
for i in range (1,no_numbers+1):
    p = random.choice(numbers)
    password = password+p

print(password)

new_l_password = ""
lenth = len(password)
i=0
while i!=9:
    
    index = random.randint(0,lenth)
    print(index)
    lenth = lenth - 1
    new_l_password = new_l_password+password[index]
    del password[index]

    if password == "":
        break
    
    i+=1

print(new_l_password)



