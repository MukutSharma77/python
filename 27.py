#Accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

#inputing comma seprated word and the printing same
string=input("Enter Comma Seprated words  :  ").split(",")
print(f"\nInputed words :   {(',').join(string)}")


#sorting the given text than printing it
print("\n Sorting given words")
string=sorted(string)

print(f"\nSorting Inputed words :   {(',').join(string)}")