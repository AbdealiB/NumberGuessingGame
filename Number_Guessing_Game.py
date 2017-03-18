'''
A Simple Number Guessing Game
by AbdealiB
https://github.com/AbdealiB/NumberGuessingGame

'''

import random
import sys

def gamePlay():
    y_n = input("\nDo you want to start the game? (Y/y/n/N) >>>> ")
    if (y_n.lower() == 'y'): # If user presses y/Y and converting it into lower case
        rnd_num = random.randint(1,10) # Generating the random number
        flag = True
        limit = 1
        for limit in range(limit,4):
            while (flag):
                    try: # Checking that input from user is a number only
                        usr_int = int(input("\nGuess a number from 1-10 >>>> "))
                        
                        # Checking if number guessed by user is correct or not
                        if (usr_int == rnd_num):
                            print("\nYou Guessed correctly.")
                            
                            # How many tries it took user to guess the number, if guessed correctly
                            if (limit==1):
                                print("\nIt took you only 1 try to Guess.")
                            else:
                                print("\nIt took you {} tries to Guess.".format(limit))
                            flag=False # Setting flag=false because user guessed the number correctly
                            
                        elif (usr_int < rnd_num): # Notifying the user that entered number is too low
                            print("\nNumber too Low.")
                            break
                            
                        elif (usr_int > rnd_num): # Notifying the user that entered number is too high
                            print("\nNumber too High.")
                            break
                            
                    # If not entered a number
                    except ValueError: 
                        print("\nPlease enter a number only.")
                        continue
                        
            # If number has not guessed yet
            if (flag != False): 
                # tries left
                print("\nNumber of tries left >>>> {}.".format(3-limit))
            limit+=1 # Incremeting the tries if the number is not guessed yet
            
        # If user was not able to guess the number in 3 tries
        if (flag != False):
            print("\nErr.. Ran out of tries.")
            print("\nOriginal Number was >>>> {}.".format(rnd_num)) # Original Number
            
    # If user presses any other key
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
