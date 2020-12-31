'''Create a function that takes a list of names and returns a list where only the first letter of each name is capitalized.
Examples
cap_me(["mavis", "senaida", "letty"]) ➞ ["Mavis", "Senaida", "Letty"]
cap_me(["samuel", "MABELLE", "letitia", "meridith"]) ➞ ["Samuel", "Mabelle", "Letitia", "Meridith"]
'''

def function(list_):
    list2=[]
    for i in list_:
        list2.append(i.upper())
    print(list2)


list_=["mavis", "senaida", "letty"]
function(list_)