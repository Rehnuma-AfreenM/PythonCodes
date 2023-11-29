def is_leap(year):
    leap = False

    if year % 4 != 0:     # Write your logic here
        print(leap)
    else:
        print(True)
    return leap


year = int(input())
is_leap(year)
