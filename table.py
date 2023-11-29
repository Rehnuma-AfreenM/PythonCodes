# Table generator without using loop.
"""
x = int(input("Enter the number for the table : "))
print("{} * 1 = {} ".format(x, x*1))
print("{} * 2= {} ".format(x, x*2))
print("{} * 3= {} ".format(x, x*3))
print("{} * 4= {} ".format(x, x*4))
print("{} * 5= {} ".format(x, x*5))
print("{} * 6= {} ".format(x, x*6))
print("{} * 7= {} ".format(x, x*7))
print("{} * 8 = {} ".format(x, x*8))
print("{} * 9 = {} ".format(x, x*9))
print("{} * 10 = {} ".format(x, x*10))
"""
# Table generator using loop.

x = int(input("Enter the number for the table : "))
for i in range(1, 11):
    print("{} * {} = {} ".format(x, i, x * i))
