'''Valid Hex Code
Create a function that determines whether a string is a valid hex code.
A hex code must begin with a pound key # and is exactly 6 characters in length. Each character must be a digit from 0-9 or an alphabetic character from A-F. All alphabetic characters may be uppercase or lowercase.
Examples
is_valid_hex_code("#CD5C5C") ➞ True
is_valid_hex_code("#EAECEE") ➞ True
is_valid_hex_code("#eaecee") ➞ True
is_valid_hex_code("#CD5C58C") ➞ False
is_valid_hex_code("#CD5C5Z") ➞ False
is_valid_hex_code("#CD5C&C") ➞ False
is_valid_hex_code("CD5C5C") ➞ False
'''

def is_valid_hex_code(hexa):
   count=0
   hexa=hexa.upper()
   if hexa[0]=='#':
       count+=1
   else:
       count-=1


   for i in range(len(hexa)):


         if hexa[i] in 'ABCDEF' and len(hexa)==7 :
             count+=1

         elif hexa[i].isdigit():
             count+=1


   if count==len(hexa):
        print(True)
   else:
        print(False)

is_valid_hex_code("#CD5C5C")
is_valid_hex_code("#EAECEE")
is_valid_hex_code("#eaecee")
is_valid_hex_code("#CD5C58C")
is_valid_hex_code("#CD5C5Z")
is_valid_hex_code("#CD5C&C")
is_valid_hex_code("CD5C5C")
