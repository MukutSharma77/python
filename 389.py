'''Semantic Versioning
In semantic versioning a piece of software can be represented in a format like this example: 6.1.9.
The first number is the major version.
The second number is the minor version.
The third number is the patch (bug fixes).
Create three separate functions, one to retrieve each element in the semantic versioning specification.
Examples
# 6.1.9
retrieve_major("6.1.9") ➞ "6"
retrieve_minor("6.1.9") ➞ "1"
retrieve_patch("6.1.9") ➞ "9"
'''

major=('6.1.9').split('.')

list_=[]
for i in range(0,len(major)):
    if major[i] not  in list_:
        print(major[i])
        list_.append(major[i])

