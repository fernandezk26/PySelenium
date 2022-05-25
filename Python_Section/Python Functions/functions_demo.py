from decimal import DivisionByZero


def calculator(symbol, number1, number2):
    if symbol == '+':
        calculation = number1 + number2
    elif symbol == '-':
        calculation = number1 - number2
    elif symbol == '/':
        try:
            calculation = number1/number2
            print(f" the result is {calculation}")
        except(DivisionByZero):
            print("Cannot divide by zero")
    elif symbol == '*':
        calculation = number1 * number2
    return calculation

print("Welcome to the calculator \n")
symbol = input("Type '+' if you want to add, \n'-' if you want to subtract, \n '/' if you want to divide, \n '*' if you want to multiply: ")
number1 = int(input("Enter the first nubmer: "))
number2 = int(input("Enter the second number: "))

print(calculator(symbol, number1, number2))

#parameters can have a default value
#keyword parameter - when a default value is used
#positional parameter - when default value is not used
#syntax:
# def verify_process_completes(timeout=60):
#     <code here>
#     return<something>

# #calling the function:
# verify_process_completes(timeout-120) - uses a positional parameter
# verify_process_completes() -  uses a default keyword parameter