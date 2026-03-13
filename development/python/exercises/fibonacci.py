""" Calculates the Fibonacci number at a given position"""

# The program asks the user for a number.
numero = int(input("Ingrese numero: "))

# It starts with the first two Fibonacci numbers:
a = 0
b = 1

# Using a loop, the script repeatedly updates these values so that:
for i in range(numero+1):
    if i == numero: #When the loop reaches the position requested by the user, it prints the Fibonacci value.
        print(a)
    
    temp_a = b
    temp_b = a + b

    a = temp_a
    b = temp_b