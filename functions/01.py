# Function with parameters and return value
# Function's use the def key word and function name
# Functions may use parameters and return a value
def add_numbers(a,b): # Passing two parameters 
    return a + b  # Returning the sum of two numbers

result = add_numbers(5,5)
print(f"Sum: {result}")


# Local scope

def greet():
    message = "Hello World"
    print(message)
greet()
#print(message) #message is not defined out scope

# Global scope

greeting = "Hi"

def say_hello():
    print(greeting + " from inside the function")
say_hello()
print(greeting + " from outside the function")
