student_score=input("Input a list of student sccore ").split()
for n in range(0,len(student_score)):
    student_score[n]=int(student_score[n])
    
max_score=0    
for score in student_score:
    if score>max_score :
        max_score=score
print(f"The Heighest score is  {max_score}")            