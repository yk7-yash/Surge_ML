# Q1. Matrix Multiplication using List

# First Matrix
print("\nMatrix Multiplication\nFirst Matrix:")
m1 = int(input("Enter M for M x N matrix: "))
n1 = int(input("Enter N for M X N matrix: "))

# Create a zero matrix with rows and columns from user input
matrix1 = [[0 for j in range(n1)] for i in range(m1)]
for i in range(m1):
    for j in range(n1):
        matrix1[i][j] = int(input("Enter an element: "))

# Display the first matrix
print("\nMatrix form:")
for i in range(m1):
    for j in range(n1):
        print(matrix1[i][j], end="\t")
    print("")

# Second Matrix
print(
    "\nNote: For Matrix Multiplication the no. of rows of second matrix must be equal to the no. of columns of first matrix")
print("\nSecond Matrix")
# Number of Rows of Second Matrix
m2 = n1
print("The number of rows in the Second Matrix is", m2)
n2 = int(input("Enter N for M X N matrix: "))

# Create a zero matrix with columns from user input
matrix2 = [[0 for j in range(n2)] for i in range(m2)]
for i in range(m2):
    for j in range(n2):
        matrix2[i][j] = int(input("Enter an element: "))

# Display the second matrix
print("\nMatrix form:")
for i in range(m2):
    for j in range(n2):
        print(matrix2[i][j], end="\t")
    print("")

# Matrix Multiplication
# Create a zero matrix with number of rows from first matrix and number of columns from second matrix
product = [[0 for j in range(n2)] for i in range(m1)]
for i in range(m1):
    for j in range(n2):
        for k in range(m2):
            product[i][j] += matrix1[i][k] * matrix2[k][j]

# Display the Resultant Matrix
print("\nThe Resultant Matrix:")
for i in range(m1):
    for j in range(n2):
        print(product[i][j], end="\t")
    print("")