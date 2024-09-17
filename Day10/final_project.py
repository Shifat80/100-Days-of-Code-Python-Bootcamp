
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    num1=int(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
        
    should_continue=True    

    while should_continue:    
        operations_symbol = input("Pick an operation from the line above: ")
        num2=int(input("What's the second number?: "))
        calculator_function = operations[operations_symbol] 
        ans=calculator_function(num1,num2)
        print(f"{num1} {operations_symbol} {num2} = {ans}")

        if input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: ")=="y":
            num1=ans
        else:
            should_continue=False  
            calculator() 

  
  
calculator()  