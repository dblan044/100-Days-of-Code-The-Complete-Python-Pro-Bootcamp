# Ask for operation, second number and continuing on a loop
# Result prints after second number is inputed
#     operation done in floating point
# Ask to continue calculating or start a new calculation
#     if yes, ask for another number to operate on previous result
#     if no, ask anew for a first number and loop everything again

import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

restart = True
while restart:
    print(art.logo)
    should_accumulate = True
    first_number = float(input("What's the first number?: "))

    while should_accumulate:

        operation = input("+\n-\n*\n/\nPick an operation: ")
        second_number = float(input("What's the second number?: "))

        result = 0.0
        if operation == "+":
            result = float(operation_dict["+"](first_number, second_number))
            print(f"{first_number} + {second_number} = {result}")
        elif operation == "-":
            result = float(operation_dict["-"](first_number, second_number))
            print(f"{first_number} - {second_number} = {result}")
        elif operation == "*":
            result = float(operation_dict["*"](first_number, second_number))
            print(f"{first_number} * {second_number} = {result}")
        else:
            result = float(operation_dict["/"](first_number, second_number))
            print(f"{first_number} / {second_number} = {result}")

        to_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if to_continue == "y":
            first_number = result
        else:
            should_accumulate = False
            print("\n" * 20)
