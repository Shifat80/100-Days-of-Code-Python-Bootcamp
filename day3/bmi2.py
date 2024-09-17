weight=input("what is your weight?\n")
height=input("What is your height in cm?\n")
a=int(weight)/int(height)**2
BMI=round(a,2)
if BMI>18:
    print("Underweight")
elif 18>BMI>25:
    print("Normal Weight")
else:
    print("over weight\n")    
