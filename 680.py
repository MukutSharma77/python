'''Complete the Binary Number
Create a function which adds zeros to the start of a binary string, so that its length is a mutiple of 8.
Examples
complete_binary("1100") ➞ "00001100"
complete_binary("1101100") ➞ "01101100"
complete_binary("110010100010") ➞ "0000110010100010"
Notes
Return the same string if its length is already a multiple of 8.'''

bin_="1100"
zeros=len(bin_)%8

print(str('0' * zeros ) + bin_)