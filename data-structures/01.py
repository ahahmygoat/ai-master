numbers = [1,2,3,4,5]
fruits= ["Apple", "Mango", "Orange"]

mixed = ["1", 5, True]
print(numbers[0]) # Prints the first element
# We access the first element by the index [loc]

# Adding elements into list
fruits.append("grape") # Adds to the end of the list
fruits.insert(1, "cherry") # Adds element at index 1 in the list

# Remove elements from a list

fruits.remove("Apple")

del fruits[0] # deletes at index 0 from list
fruits.pop() # Removes the last item in the list

print(fruits)

# Slice a list of items
# Getting elements from a particular place
sliced_numbers = numbers[1:3] # returns numbers from index 1 to 3. 1 to before 3
print(sliced_numbers)

# Tuple

colors = ("Red, white, blue")
single_item = ("bmw",) # Must put a , for single item tuple
print(colors[0]) # it is an ordered DS so index

# A list of tuples could be modified otehrwise tuples are immutable

# Dictonaires

student = {"name": "John", "age": 15, "grade": "A"}
print(student['grade']) # Pass the key to print or access the value
student["subject"] = "Math" # Adds a new key and assigns a value
print(student)

# Delete a certain key

del student['grade']

student.pop('subject')
print(student)

# Create a list from key value paris then interate overthem and display the values
student = {"name": "John", "age": 15, "grade": "A"}
for key, value in student.items():
    print(key, value)
    
    
    
# Sets

numbers = {1,2,3,4} # un ordered unqiue if no key value {} = set
name_set = set()
numbers.add(5)
print(numbers)
numbers.add(6)
numbers.remove(2)
print(numbers)


set1 = {1,2,3}
set2 = {3,4,5}

# Union put the sets togeteher
print(set1 | set2)
# intersection returns the common element in both
print(set1 & set2)
# Difference from first set what is different from second one: 
print(set1 - set2)

