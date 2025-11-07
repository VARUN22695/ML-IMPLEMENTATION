number = int(input("Enter a number: "))

result = 1
counter = 1

while counter <= number:
    result *= counter  # Step through this to see result build
    counter += 1       # Counter increments

print(f"Factorial of {number} is {result}")
