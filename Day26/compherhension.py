numbers=[1,2,3,4,5,6,7,8,9,10]

new_list=[n**2 for n in numbers]

result=[n for n in numbers if n%2==0]

print(result)

print(new_list)