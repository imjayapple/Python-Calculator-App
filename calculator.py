#define the 4 arithmetic operations, add/subtract/multiply/divide

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

#guide user choice towards one of the 4 operations
#capture that choice and then seek the desired input of num1 & num2 from the user to perform the next operation
#if/else statement prints the numbers being used (num1, num2), the operation being performed, and the resultant

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter your second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid input")

#i have not seen this before in my learning material but apparently this line allows the script to be run as a standalone program

if __name__ == "__main__":
    main()