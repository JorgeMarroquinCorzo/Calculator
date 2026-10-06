# My calculator program!!

print("Welcome to my calculator!")
print("Choose an operation below!")

# Dictionary mapping choices to operation names
operations = {
    "1": "Addition",
    "2": "Subtraction",
    "3": "Multiplication",
    "4": "Division"
}

while True:
    print("\n----------------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("\n----------------")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == "5":
        print("Goodbye!!!!")
        break             # <--- Stops the loop

    if choice in operations:
        # Announce the choice IMMEDIATELY before asking for numbers
        print(f"You chose {operations[choice]}")

        # Catch non-numeric inputs for the numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue  # Restarts the loop from the top

        if choice == "1":
            result = num1 + num2
            print("The answer is:", result)

        elif choice == "2":
            result = num1 - num2
            print("The answer is:", result)

        elif choice == "3":
            result = num1 * num2
            print("The answer is:", result)

        elif choice == "4":
            if num2 == 0:
                print("You can't divide by zero!")
            else:
                result = num1 / num2
                print("The answer is:", result)

    else:
        print("Invalid choice! Please select 1, 2, 3, 4, or 5.")