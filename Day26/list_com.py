# FOR LOOP
num=[1,2,3]
new=[]
for n in num:
    add_1=n+1
    new.append(add_1)
print(new)    

# OR
# LIST COMPREHENSION
new=[n+1 for n in num]
print(new)

# string as list
name="shifat"
letter_list=[letter for letter in name]
print(letter_list)

# Range as list

names=["shifat","rahim","sakib","safi","mushfiq"]

short_names=[name for name in names if len(name)<=4]
print(short_names)



# converting upper case
long_names=[name.upper() for name in names if len(name)>=4]
print(long_names)