'''Convert to Hex
Create a function that takes a strings characters as ASCII and returns each characters hexadecimal value as a string.
Examples
convert_to_hex("hello world") ➞ "68 65 6c 6c 6f 20 77 6f 72 6c 64"
convert_to_hex("Big Boi") ➞ "42 69 67 20 42 6f 69"
convert_to_hex("Marty Poppinson") ➞ "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"'''

def convert_to_hex(string):
    string=string.split()
    for i in string:
        for j in i:
            hexi_=str(hex(ord(j)))
            print(hexi_[2:],end=" ")
    print()


convert_to_hex("hello world")
convert_to_hex("Big Boi")
convert_to_hex("Marty Poppinson")