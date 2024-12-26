import os
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '%': mod
}
def calculator():
    num1 = float(input("enter first number:"))
    for symbol in operations:
        print(symbol)

    wanna_continue = True
    while wanna_continue:
        operator = input("pick an operation:")
        num2 = float(input("enter next number:"))

        calculator_function = operations[operator]
        output = calculator_function(num1,num2)
        print(f"{num1} {operator} {num2} = {output}")

        next = input(f"enter y to continue calculation with {output}, n to continue calculation with fresh number, or x to exit:").lower()
        if next == "y":
            num1 = output
        elif next == "n":
            wanna_continue = False
            os.system('cls')
            calculator()
        else:
            wanna_continue = False
            print("Have a nice day")
calculator()
