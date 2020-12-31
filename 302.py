'''Letters Only
Write a function that removes any non-letters from a string, returning a well-known film title.
Examples
letters_only("R!=:~0o0./c&}9k`60=y") ➞ "Rocky"
letters_only("^,]%4B|@56a![0{2m>b1&4i4") ➞ "Bambi"
letters_only("^U)6$22>8p).") ➞ "Up"'''


def function(string):
    s=""
    for i in string:
        if i.isalpha():
            s+=i

    print(s)


string="^,]%4B|@56a![0{2m>b1&4i4"
function(string)