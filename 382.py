'''Create a function that filters out a list of state names into two categories based on the second parameter.
len(x)>2 ---> fiull
 len(x) == 2 --> abb
Abbreviations abb
Full names full
Examples
filter_state_names(["Arizona", "CA", "NY", "Nevada"], "abb")
➞ ["CA", "NY"]
filter_state_names(["Arizona", "CA", "NY", "Nevada"], "full")
➞ ["Arizona", "Nevada"]
'''

list_=["Arizona", "CA", "NY", "Nevada"]
list_1=[]
list_2=[]
for i in list_:
    if len(i) > 2:
        list_1.append(i)
    else:
        list_2.append(i)

print(list_1)
print(list_2)