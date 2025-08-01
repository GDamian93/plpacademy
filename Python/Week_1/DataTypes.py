import random

# Numeric Data Types
age = 25  # int
height = 5.9  # float  
complex_number = 3 + 4j  # complex      
# Sequence Data Types
name = "Alice"  # str   
fruits = ["apple", "banana", "cherry"]  # list
coordinates = (10.0, 20.0)  # tuple
unique_numbers = {1, 2, 3, 4}  # set
decimal_digits = range(10) # 

# Mapping Data Type
person = {"name": "Alice", "age": 25}  # dict
# Boolean Data Type
is_student = True  # bool
# None Type
nothing = None  # NoneType

# type() function: used to get the data type of any object.
# Displaying the data types
print("Value and Data Types:")                                # Output:
print("age:", age, type(age))                                 # Data Types:
print("height:", height, type(height))                        # age: <class 'int'>
print("complex_number:",complex_number, type(complex_number)) # height: <class 'float'>
print("name:", name, type(name))                              # complex_number: <class 'complex'>   
print("fruits:", fruits, type(fruits))                        # fruits: <class 'list'>
print("coordinates:", coordinates, type(coordinates))         # coordinates: <class 'tuple'>
print("unique_numbers:", unique_numbers, type(unique_numbers))# unique_numbers: <class 'set'>
print("decimal_digits:", decimal_digits, type(decimal_digits))# decimal_digits: <class 'range'>
print("person:", person, type(person))                        # person: <class 'dict'>
print("is_student:", is_student, type(is_student))            # is_student: <class 'bool'>
print("nothing:", nothing, type(nothing))                     # nothing: <class 'NoneType'>


print(random.randrange(1, 10))








# Note: The output will show the type of each variable as defined above.    
