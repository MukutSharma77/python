'''Count the Number of Duplicate Characters
Create a function that returns the amount of duplicate characters in a string. It will be case sensitive and spaces are included. If there are no duplicates, return 0.
Examples
duplicates("Hello World!") ➞ 3
# "o" = 2, "l" = 3.
# "o" is duplicated 1 extra time and "l" is duplicated 2 extra times.
# Hence 1 + 2 = 3
duplicates("foobar") ➞ 1
duplicates("helicopter") ➞ 1
duplicates("birthday") ➞ 0
# If there are no duplicates, return 0'''

def duplicates(string):
    count=0
    str_=''
    for i in string:
        if i not in str_ and string.count(i) > 1:
            str_+=i
            count+=1



    print(count)

duplicates("Hello World!")
duplicates("foobar")
duplicates("helicopter")
duplicates("birthday")