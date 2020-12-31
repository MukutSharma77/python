'''Create a function where given the number n to count down from, and some words txt, return a countdown sequence as a string
countdown(10, "Blast Off") ➞ "10. 9. 8. 7. 6. 5. 4. 3. 2. 1. BLAST OFF!"'''

import time

def countdown(no,msg):
    for i in range(no,0,-1):
        print(i,", ",end="  ")
    print(msg," ! ")



# inputing bumber and messgae and call a function
no=int(input("Enter CountDown number :   "))
msg=input("Enter Message  :    ")
countdown(no,msg)