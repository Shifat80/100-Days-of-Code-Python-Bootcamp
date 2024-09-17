student_height=input("Input a list of student heights ").split()
for n in range(0,len(student_height)):
    student_height[n]=int(student_height[n])
# sum_of_height=sum(student_height) 
total_height=0
for height in student_height:
    total_height+=height
avg=total_height/len(student_height)
print(round(avg))
