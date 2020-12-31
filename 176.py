#Is the String in Order

string=input('Enter String   :               ')
string_=string
string=sorted(string)
if string_==("").join(string):
    print("Yes string is  sorted")

else:
    print("No string is not in sorted")
