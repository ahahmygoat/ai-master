
num = int(input("Enter a number: ")) # ask user for number type cast response into number

if num > 1: # Check if number is > 1 prime numbers are numbers greater than 1 
    for i in range(2,int(num**0.5) +1): # sqrt if number is not div..
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
        else:
            print(f"{num} is a prime number")            
else:
    print(f"{num} is not a prime number")
    
    
    
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mult(a,b):
    return a * b
def div(a,b):
    if b != 0: # Cannot divide by 0
        return a / b
    else:
        return "Division by zero is not allowed"
    
while True: # Will run true forever unless you add a break
    print("\nMenu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choices = ["1", "2","3","4","5"] # Create a list of possible choices in the menu
    choice = input ("Enter in your choice: ")
    if choice not in choices:
        print("Invalid Choice. Please select a number between 1 and 5")
        continue
        
    if choice == "5":
        print("Exiting Program.")
        break
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    if choice == "1":
        print(f"Result: {add(num1, num2)}")
    elif choice == "2":
        print(f"Result: {sub(num1, num2)}")
    elif choice == "3":
        print(f"Result: {mult(num1, num2)}")
    elif choice == "4":
        print(f"Result: {div(num1, num2)}")
