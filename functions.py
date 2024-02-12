# Inbuilt functions
y = max(67, 56, 34, 89, 23)
print(y)

x = min(67, 56, 34, 89, 23)
print(x)

z = pow(2, 3)
print(z)


# User-defined functions
def details():
    print("Gloria")


details()  # Calling a function


# Parameters and Arguments
def student(name, course, age):
    print(name, course, age)


student("Ashley", "MIT", "17")
student("Goretty", "Cybersecurity", "18")


def employees(fullname, Idnumber, Salary, Position, age):
    print(fullname, Idnumber, Salary, Position, age)


employees("Dcee Darlton", 2010127, "20000", "Secretary", 20)
employees("Kanye West", 2010128, "50000", "Chairman", 24)
employees("Pop Smoke", 2010130, "80000", "Treasurer", 28)
employees("Ty Dolla", 2010183, "25000", "Operations Manager", 20)
employees("Princess Diana", 2010257, "16500", "Receptionist", 20)
