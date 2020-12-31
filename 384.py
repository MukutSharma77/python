'''Create a function which takes in a word and spells it out, by consecutively adding letters until the full word is completed.
Examples
spelling("bee") ➞ ["b", "be", "bee"]
spelling("happy") ➞ ["h", "ha", "hap", "happ", "happy"]'''

string=input("Enter String :  ")

list_=[]
for i in range(1,len(string)+1):
    idx=string[:i]
    list_.append(idx)

print(list_)