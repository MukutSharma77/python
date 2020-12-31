'''Guessing game with random winning number and if a user is guessing higher than winning number
than print('You guessed to high') else  print('You guessed to low') '''

import random

winning_num=random.randint(1,20)
i=1
while True:
    guessing_num=int(input("Guess the number :  "))
    if guessing_num==winning_num:
        print("Congratulations")
        print(f"You won in ",i,' times ')
        break

    elif guessing_num>0 and guessing_num<=20:
        # print('Lost')
        if guessing_num>winning_num:
            print('You Guessed to high ')

        else:
            print('You guessed to low')
        print("try more")

    else:
        print("wrong input")

    i+=1