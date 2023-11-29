from random import shuffle
#First function block.

def shuffleList(orgList):
    shuffle(orgList)
    return orgList

#Second function block.

def players_guess():
    guess = ''
    
    while guess not in ['0','1','2']:
        guess = input('pick an cup 0,1,2: ')
        
    return int(guess)      

#Third function block.

def checking_guess(orgList,guess):
    if orgList[guess] == '0':
        print('correct')
    else:
        print('wrong!')
        print(orgList)


#mylist
orgList=[' ','0',' ']
#newlist
newList = shuffleList(orgList)
#guess
guess = players_guess()
#checkguess
checking_guess(newList,guess)