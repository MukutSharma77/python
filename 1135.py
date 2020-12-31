'''N-Length Letter Groups
Write a function that returns a list of strings populated from the slices of n-length characters of the given word (a slice after another while n-length applies onto the word).
Examples
collect("intercontinentalisationalism", 6)
➞ ["ationa", "interc", "ntalis", "ontine"]
collect("strengths", 3)
➞ ["eng", "str", "ths"]
collect("pneumonoultramicroscopicsilicovolcanoconiosis", 15)
➞ ["croscopicsilico", "pneumonoultrami", "volcanoconiosis"]'''


def collect(str_,num):
    lst=[]
    for i in range(0,len(str_),num):
        lst.append(str_[i:i+num])
    print(lst)



collect("intercontinentalisationalism", 6)
collect("strengths", 3)
collect("pneumonoultramicroscopicsilicovolcanoconiosis", 15)