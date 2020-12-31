'''Pluralize!
Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.
Examples
pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }
pluralize(["table", "table", "table"]) ➞ { "tables" }
pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }'''

def pluralize(lst):
    set_=[]
    for i in lst:
        if lst.count(i)>1 and i not in set_:
            set_.append(i+'s')
        else:
            set_.append(i)
    print(set(set_))


pluralize(["cow", "pig", "cow", "cow"])
pluralize(["table", "table", "table"])
pluralize(["chair", "pencil", "arm"])