#simple calculator with basic arithmetic operations (CodSoft)

def calculator():
    while True:
        print("\n=== Do Your Calculations with your Simple Calculator ===")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("\nEnter operation (1-5): ")
        
        if choice == '5':
            print("Thank you for using the calculator!")
            break
            
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please select 1-5")
            continue
            
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: Please enter valid numbers!")
            continue

        result = None
        if choice == '1':
            result = num1 + num2
            operation = '+'
        elif choice == '2':
            result = num1 - num2
            operation = '-'
        elif choice == '3':
            result = num1 * num2
            operation = '*'
        elif choice == '4':
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                continue
            result = num1 / num2
            operation = '/'
        
        print(f"\nResult: {num1} {operation} {num2} = {result:.2f}")
        
        while True:
            continue_calc = input("\nDo you want to continue? (y/n): ")
            if continue_calc in ['y', 'n']:
                break
            print("Please enter 'y' for yes or 'n' for no")
            
        if continue_calc == 'n':
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    calculator()