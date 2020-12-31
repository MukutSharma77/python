'''Filter Repeating Character Strings
Create a function that keeps only strings with repeating identical characters (in other words, it has a set size of 1).
Examples
identical_filter(["aaaaaa", "bc", "d", "eeee", "xyz"])
➞ ["aaaaaa", "d", "eeee"]
identical_filter(["88", "999", "22", "545", "133"])
➞ ["88", "999", "22"]
identical_filter(["xxxxo", "oxo", "xox", "ooxxoo", "oxo"])
➞ []'''


list_=["aaaaaa", "bc", "d", "eeee", "xyz"]

list_result=[i for i in list_ if i.count(i[0])==len(i)]
print(list_result)