#Replace Every Blank Space with Hyphen

#inputing string
string=input("Enter String :   ")

#if spacen in string hyphen it

if " " in string:
    string=string.replace(" ","_")
    print(string)
else:
    print("No Blank Space")