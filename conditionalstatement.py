temperature = 32
if temperature > 37:
    print("It is hot")
else:
    print("It is cold")

# A program that prints the largest number among three numbers
num1 = 45
num2 = 89
num3 = 32
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")

# A program that checks whether a number is even or odd
number = 56
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# A program that checks whether a number is prime or not
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)):
        if num % i == 0:
            return False
        return True


# Test the function
num = 91
if is_prime(number):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")



