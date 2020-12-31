'''List from Comma-Delimited String
Write a function that turns a comma-delimited list into an array of strings.
Examples
to_array("watermelon, raspberry, orange")
➞ ["watermelon", "raspberry", "orange"]
to_array("x1, x2, x3, x4, x5")
➞ ["x1", "x2", "x3", "x4", "x5"]'''

string=input("Enter string comma seprated  :   ").split(",")
print(string)