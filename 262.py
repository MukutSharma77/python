'''In the Code tab is a function which is meant to return how many uppercase letters there are in a list of various words. Fix the list comprehension so that the code functions normally!
Examples
count_uppercase(["SOLO", "hello", "Tea", "wHat"]) ➞ 6
count_uppercase(["little", "lower", "down"]) ➞ 0'''

def functon(list_):
    count=0
    for i in list_:
        for j in i:
            if j.isupper():
                count+=1
    print(count)



list_=["SOLO", "hello", "Tea", "wHat"]
functon(list_)