# Example 1: Checking a condition
num = 15
print("Example #1: \n")
if num > 10:
    print("Positive Number")
elif num == 0: # Else if we can have multiple condition
    print("Number = 0")
else:
    print("Negative Number")


# Example 2: Nested Conditions
print("Example #2: \n")
age = 25
if age > 18:
    if age < 30:
        print("Young Adult")
    else:
        print("Adult")

# Example 3: Loop through a list
print("Example #3: \n")
fruits = ["aaple", "orange", "mango"]
for fruit in fruits:
    print(fruit)

# Example 4: Loop with range
print("Example #4: \n")
for i in range(10):
    print(i) # This wil print 0-9
    
# Example 5: While loop
# Count down from 5
print("Example #5: \n")
count  = 5
while count > 0:
    print(count)
    count -= 1 # Short cut the decrement operator reduce by 1
# Should print 0-4

# Example 6: Break breaks a for loop
print("Example #6: \n")
for i  in range(10):
    if i == 5:
        break
    print(i)

# Example 7: Continue to move to the next iteration skip (#7)
print("Example #7: \n")
for i  in range(10):
    if i == 7:
        continue
    print(i)
# Example 8: Use continue to print odd numbers
print("Example #8: \n")
for i  in range(10):
    if i %2 == 0:
        continue
    print(i)