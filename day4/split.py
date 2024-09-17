import random
names=input("Give me everyones's name? ")
name=names.split(", ")
list_iteam=len(name)
# random_choice=random.randint(0,list_iteam-1)

print(random.choice(name))
