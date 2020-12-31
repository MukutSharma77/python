'''Count the Number of Duplicate Characters
Create a function that takes a string and returns the number of alphanumeric characters that occur more than once.
Examples
duplicate_count("abcde") ➞ 0
duplicate_count("aabbcde") ➞ 2
duplicate_count("Indivisibilities") ➞ 2
duplicate_count("Aa") ➞ 0
'''

def function(string):
    string_=''
    count=0
    for i in string:
        if  string.count(i) > 1:
            if i not in string_:
                count+=1
                string_+=i

    print(count)


string="aabbcde"
function(string)