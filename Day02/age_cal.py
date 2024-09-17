age=input("what is your age?")
age_in_int=int(age)
remaining_age=90-age_in_int
remains_month=remaining_age*12
remains_days=remaining_age*365
remains_weeks=remaining_age*52
print(f"you have {remains_weeks} weeks, {remains_days} days, {remains_month} months left to live")