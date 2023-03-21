#define the 4 arithmetic operations, add/subtract/multiply/divide

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def exponent(x, y):
    return x ** y

def percent(x, y):
    return (x / y) * 100

#guide user choice towards one of the 4 operations
#capture that choice and then seek the desired input of num1 & num2 from the user to perform the next operation
#if/else statement prints the numbers being used (num1, num2), the operation being performed, and the resultant

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent")
    print("6. Percent")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter your second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        result = divide(num1, num2)
        if isinstance(result, str):
            print(result)
        else:
            print(num1, "/", num2, "=", result)
    elif choice == '5':
        print(num1, "to the power of ", num2, "=", exponent(num1, num2))
    elif choice == '6':
        print(num1, "% of ", num2, "=", percent(num1, num2))
    else:
        print("Invalid input")

#i have not seen this before in my learning material but apparently this line allows the script to be run as a standalone program

if __name__ == "__main__":
    main()
