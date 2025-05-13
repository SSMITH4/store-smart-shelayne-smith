def main():
    # Get input from user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Get sum
    total = num1 + num2
    
    # Show result
    print(f"The sum of {num1} and {num2} is {total}")

    # Show max number
    print(f"The largest of the two numbers is {max(num1, num2)}")

    # Show min number
    print(f"The smallest of the two numbers is {min(num1, num2)}")

if __name__ == "__main__":
    main()