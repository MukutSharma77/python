'''Word Endings
Create a function that adds a string ending to each member in a list.
Examples
add_ending(["clever", "meek", "hurried", "nice"], "ly")
➞ ["cleverly", "meekly", "hurriedly", "nicely"]
add_ending(["new", "pander", "scoop"], "er")
➞ ["newer", "panderer", "scooper"]'''


list_=["clever", "meek", "hurried", "nice"]
end=input("End with :  ")
list2=[]
for i in list_:
    list2.append(i+end)

print(list2)