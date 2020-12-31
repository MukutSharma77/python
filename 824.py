'''Buggy Uppercase Counting
In the Code tab is a function which is meant to return how many uppercase letters there are in a list of various words. Fix the list comprehension so that the code functions normally!
Examples
count_uppercase(["SOLO", "hello", "Tea", "wHat"]) ➞ 6
count_uppercase(["little", "lower", "down"]) ➞ 0
count_uppercase(["EDAbit", "Educate", "Coding"]) ➞ 5'''

def count_uppercase(lst):
    tot=0
    for i in lst:
        for ch in i:
            if ch.isupper():
                tot+=1
    print(tot)

count_uppercase(["SOLO", "hello", "Tea", "wHat"])
count_uppercase(["little", "lower", "down"])
count_uppercase(["EDAbit", "Educate", "Coding"])