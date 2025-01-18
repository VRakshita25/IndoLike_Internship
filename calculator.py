import math

def calculator():
    print('''  
    1. Addition  
    2. Subtraction  
    3. Multiplication  
    4. Division  
    5. Modulus  
    6. Square root   
    7. Exponent  
    ''')

    while True:
        # Get the user's choice of operation
        try:
            choice = int(input("Which mathematical operation do you want to do? "))
            if choice not in range(1, 8):  # Validating choice
                print("Invalid choice. Please select a number between 1 and 7.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue

        # Get user input for numbers
        try:
            if choice == 6:  # For square root, we only need one number
                num1 = float(input("Enter the number for square root: "))
                num2 = None  # We don't need a second number for square root
            else:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid number input. Please enter valid numeric values.")
            continue

        # Perform the chosen operation
        if choice == 1:
            add = num1 + num2
            print(f"{num1} + {num2} = {add}")
        elif choice == 2:
            difference = num1 - num2
            print(f"{num1} - {num2} = {difference}")
        elif choice == 3:
            product = num1 * num2
            print(f"{num1} * {num2} = {product}")
        elif choice == 4:
            try:
                quotient = num1 / num2
                print(f"{num1} / {num2} = {quotient}")
            except ZeroDivisionError:
                print("Division by zero not allowed!!")
        elif choice == 5:
            modulus = num1 % num2
            print(f"{num1} % {num2} = {modulus}")
        elif choice == 6:
            if num1 < 0:  # Handle negative numbers for square root
                print("Square root is not defined for negative numbers in real numbers.")
            else:
                sqrt1 = math.sqrt(num1)
                print(f"Square root of {num1} = {sqrt1}")
        elif choice == 7:
            exp = num1 ** num2
            print(f"{num1} ^ {num2} = {exp}")

        # Ask if the user wants to perform another calculation
        ch = input("Do you want to do any other calculations? (y/n) ")
        if ch.lower() == "y":
            continue
        else:
            print("----Exiting----")
            break

print("~~~~~~~~~~~~ This is a Basic Calculator ~~~~~~~~~~~~")
calculator()
