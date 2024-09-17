def format_name(first_name,last_name):
    if first_name=="" or last_name=="":
        return "You did not provide valid inputs"
    first_name=first_name.title()
    last_name=last_name.title()
    return f"{first_name} {last_name}"
print(format_name(input("Enter your first name: "),input("Enter your last name: ")))