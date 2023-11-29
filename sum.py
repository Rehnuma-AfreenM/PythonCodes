x = int(input("sum of -\n1.even numbers\n2.odd numbers\n choose 1 or 2: "))
sum = 0
if (x == 1):
    for i in range(20, 101, 2):
        sum = sum+i
    print("The sum of even numbers between 20 and 100 is ", sum)
elif (x == 2):
    for i in range(20, 100, 1):
        sum = sum+i
    print("The sum of odd numbers between 20 and 100 is ", sum)
