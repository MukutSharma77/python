'''TM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
 Your task is to create a function that takes a string and returns True if the PIN is valid and False if it's not.'''


#Inputting pin by user
pin_=int(input("ENter Pin Code :    "))

#Checking the condiotion isn pin lengtg is 4 or 6 if yes than print True

if len(str(pin_)) == 4 or len(str(pin_)) == 6:
    print(True)
else:
    print(False)