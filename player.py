x = int(input("enter the number of players: "))
if (x % 5 == 0):
    team = x/5
    print("The number of teams are ", team)
    print("No players are left")
elif (x % 5 != 0):
    team = int(x/5)
    left = x-(5*team)
    print("The number of teams are ", team)
    print("Numbers of players left are ", left)
