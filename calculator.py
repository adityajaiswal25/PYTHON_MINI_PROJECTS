def art():
    logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
    return logo

    
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

def calculator():
    print(art())
    n1 = float(input('What is the first number: '))
    while True:
        print("Available operations:")
        for op in operations:
            print(op)
        ch = input('Pick an operation: ')
        if ch not in operations:
            print("Invalid operation. Please choose from the available operations.")
            continue
        n2 = float(input("What's the second number: "))
        answer = operations[ch](n1, n2)
        if isinstance(answer, str):
            print(answer)
            continue
        print(f"{n1} {ch} {n2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation, or 'q' to quit: ").lower()
        if choice == "y":
            n1 = answer
        elif choice == "n":
            calculator()
        elif choice == "q":
            return()
        else:
            print("Invalid choice. Please type 'y', 'n', or 'q'.")

calculator()


