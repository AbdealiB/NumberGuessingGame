'''
A Simple Number Guessing Game
by AbdealiB
https://github.com/AbdealiB/NumberGuessingGame

'''

import random
import sys

def gamePlay():
    y_n = input("\nDo you want to play the game? (Y/y/n/N) >>>> ")
    if (y_n.lower() == 'y'):
        rnd_num = random.randint(1,10)
        flag = True
        limit = 1
        for limit in range(limit,4):
            while (flag):
                    try:
                        usr_int = int(input("\nGuess a number from 1-10 >>>> "))
                        if (usr_int == rnd_num):
                            print("\nYou Guessed correctly.")
                            if (limit==1):
                                print("\nIt took you only 1 move to Guess.")
                            else:
                                print("\nIt took you {} moves to Guess.".format(limit))
                            flag=False
                        elif (usr_int < rnd_num):
                            print("\nNumber too Low.")
                            break
                        elif (usr_int > rnd_num):
                            print("\nNumber too High.")
                            break
                    except ValueError:
                        print("\nPlease enter a number only.")
                        continue
            if (flag != False):
                print("\nNumber of moves left >>>> {}.".format(3-limit))
            limit+=1
        if (flag != False):
            print("\nErr.. No moves left. Better Luck Next Time")
            print("\nOriginal Number was >>>> {}.".format(rnd_num))
    else:
        print("\nOk, GoodBye!")
        input("\nPress ENTER to exit")
        sys.exit(1)
    print("\nThanks For Playing.")
    input('\nPress ENTER to exit')

print("\n|-----------------------------------------------------------------------|")
print("\n|\t\t\tWelcome to Number Guessing Game\t\t\t|")
print("\n|-----------------------------------------------------------------------|")
print("\n|\t\t\tFind The Correct Number To Win.\t\t\t|")
print("\n|-----------------------------------------------------------------------|")
print("\n|\t\t\t    You get 3 Guesses Only  \t\t\t|")
print("\n|-----------------------------------------------------------------------|")
print("\n|\t\t\t\t  GoodLuck  \t\t\t\t|")
print("\n|-----------------------------------------------------------------------|")

gamePlay()
