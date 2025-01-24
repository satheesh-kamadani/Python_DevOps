# Factorial of the number

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
number = int(input("Enter the number: "))
print(f"factorial of the {number} is: {factorial(number)}")

