# Datatype

number = 60  # int
num = 34.78  # float
greeting = "Hello there"  # str
isPythonInteresting = True  # bool

# A variable with multiple values
languages = ["python", "php", "java", "kotlin"]  # List
fruits = ("apple", "banana", "pineapple")  # Tuple
countries = {"Kenya", "Ghana", "Bangladesh"}  # Set

# Dictionary
details = {
    "Firstname": "Ashley",
    "course": "MIT",
    "age": 18,
    "nationality": "USA"

}

print(number)
print(num)
print(greeting)
print(isPythonInteresting)
print(countries)
print(details)
print(details["Firstname"])
print(details["nationality"])

# Determining the datatype of a variable
print(type(details))
print(type(countries))
print(type(greeting))

# Typecasting - Converting one datatype to another
print(float(number))
print(int(num))
