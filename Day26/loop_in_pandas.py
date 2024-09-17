student_dict={
    "student":["Angela","James","Lily"],
    "score":[56,76,98]
    }
# for (i,j) in student_dict.items():
#     print(i,j)
    
import pandas

student_frame=pandas.DataFrame(student_dict)
# print(student_frame)


#Loop through rows of a data frame
# for (key,value) in student_frame.items():  
#     print(key,value)


# pandas loop

for (index,row) in student_frame.iterrows():
    # print(row.student)
    if row.student=="Lily":
        print(row.score)