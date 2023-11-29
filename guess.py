secret_number = 4
i = 0
guess_limit = 3
while i < guess_limit:
    number_guessed = int(input("guess a number! :"))
    if number_guessed == secret_number:
        print("you have guessed right\nYou Won!")
        break
    else:
        print("wrong number")
    i = i + 1
else:
    print("you failed")
