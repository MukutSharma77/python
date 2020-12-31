'''Remove The Word!
Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.
Examples
remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]
remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]
remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []'''

def remove_letters(lst , str_):
    str_=[i for i in str_]
    for i in str_:
        if i in lst:
            lst.pop(lst.index(i))

    print(lst)


remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string")
remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon")
remove_letters(["d", "b", "t", "e", "a", "i"], "edabit")