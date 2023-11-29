"""i = 1
j = 4
k = 1
print("      *")
while j >= 1 and i <= 5 and k <= 4:
    print(" " * j, "*" * i, "*" * k)
    j = j - 1
    i = i + 1
    k = k + 1
"""
# Python Program to Generate Christmas Tree Pattern


# Generating Triangle Shape
def triangleShape(n):
    for i in range(n):
        for j in range(n - i):
            print(" ", end=" ")
        for k in range(2 * i + 1):
            print("*", end=" ")
        print()


# Generating Pole Shape
def poleShape(n):
    for i in range(n):
        for j in range(n - 1):
            print(" ", end=" ")
        print("* * *")


# Input and Function Call
row = int(input("Enter number of rows: "))

triangleShape(row)
triangleShape(row)
poleShape(row)
