from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mone_mechine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()

is_on= True


while is_on:
    option =menu.get_items()
    choice=input(f"what would you like?({option}): ")
    if choice=="off":
        is_on=False
    elif choice == "report":
        coffee_maker.report()
        mone_mechine.report()
    else:
       drink =menu.find_drink(choice)
       if coffee_maker.is_resource_sufficient(drink) and mone_mechine.make_payment(drink.cost):
           coffee_maker.make_coffee(drink)
    