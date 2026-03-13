"""This script generates and prints rows of Pascal's Triangle based on a number entered by the user."""

# The program asks the user to enter a number.
numero = int(input("Ingrese numero: "))
# That number determines how many rows of the triangle will be generated.


linea_a = []

for fila in range(numero):
    linea_b = []
    for columna in range(numero):
        if fila == 0 or columna == 0: 
            # The first row and first column always contain 1.   
            linea_b.append(1) 
        else:
            # The rule used is that each number is the sum of the number above it and the number to its left.
            linea_b.append(linea_a[columna] + linea_b[columna-1])
    linea_a = linea_b # Each row is built using values from the previous row.
    print(linea_a) #Each generated row is printed to the screen.


