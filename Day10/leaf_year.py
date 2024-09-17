def leaf_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def days_in_month(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month == 2:
        if leaf_year(year):
            return 29
        else:
            return 28   
    else:
        return 30

 
 
year=int(input("Enter year: "))
month=(int(input("Enter month: ")))
days=days_in_month(year, month)
print(days)
        