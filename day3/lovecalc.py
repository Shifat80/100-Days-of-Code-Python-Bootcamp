name1=input("What's Your name?\n")
name2=input("what's your name?\n")
name=name1+name2
t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")
l=name.count("l")
o=name.count("o")
v=name.count("v")
e=name.count("e")
true=t+r+u+e
love=l+o+v+e

love_score=str(true)+str(love)
print(love_score)
if (love_score<10) or (love_score>90):
    
