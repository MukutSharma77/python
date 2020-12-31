'''Modify Words
Create a function that takes a list of any length. Modify each element (capitalize, reverse, hyphenate).
Examples
edit_words(["new york city"]) ➞ ["YTIC KR-OY WEN"]
edit_words(["null", "undefined"]) ➞ ["LL-UN", "DENIF-EDNU"]
edit_words(["hello", "", "world"]) ➞ ["OLL-EH", "-", "DLR-OW"]
edit_words([""]) ➞ ["-"]
'''

def edit_words(lst):

    output=[]
    for i in lst:
        i=i.upper()
        output.append(i[:len(i)//2] +'-' + i[len(i)//2 :])

    for i in range(len(output)):
        output[i]=output[i][::-1]

    print(output)

edit_words(["new york city"])
edit_words(["null", "undefined"])
edit_words(["hello", "", "world"])
edit_words([""])
