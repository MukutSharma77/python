'''Create a function that will return a four-character ID using the person's first name and last name. The first character will be the first letter of the first name but in lowercase. The next three characters will be the first three characters of the last name, but the first letter will be capitalized and the other two will be in lower case.
Examples
create_id("mary", "lamb") ➞ "mLam"
create_id("John", "SMITH") ➞ "jSmi"
create_id("mary", "smith") ➞ "mSmi"

'''


string1=input("Enter Name :  ")

string2=input("Enter Last Name :  ")
print(string1[0]+string2[:3])