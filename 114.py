'''Exercise 9: Guessing Game One
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the
number, then tell them whether they guessed too low, too high, or exactly right. '''

#random to change winning value each time
import random
print("\t\t\tGuessing Game (1 to 10 )")

winning_no = random.randint(1,10)


#Using Loop Till the gussing number is equal toi winning number than break
while True:
    guessing_no=int(input("Guess the number :   "))
    if winning_no== guessing_no:
        print("You Win")
        break
    else:
        if winning_no > guessing_no:
            print("Too Low")
        elif winning_no < guessing_no:
            print("Too High")
        else:
            pass
