import random
latter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

number=['0','1','2','3','4','5','6','7','8','9']

symbol=['!','@','#','$','%','^','&','*','(',')']
print("Welcome to the PyPassword Generator!")

no_letter=int(input("How many letter would you like in your password?\n"))
no_symbol=int(input("How many symbols would you like in your password?\n"))
no_number=int(input("How many numbers would you like in your password?\n"))
# easy level
# password=""
# for xhar in range(1,no_letter+1):
#     password+=random.choice(latter)
# for char in range(1,no_symbol+1):
#     password+=random.choice(symbol)    
# for char in range(1,no_number+1):
#     password+=random.choice(number)    

    
# print(password)    
password_list=[]
for char in range(1,no_letter+1):
    password_list.append(random.choice(latter))
for char in range(1,no_symbol+1):
    password_list.append(random.choice(symbol))
for char in range(1,no_number+1):
    password_list.append(random.choice(number))
random.shuffle(password_list)
password=""

for char in password_list:
    password+=char
print(password)