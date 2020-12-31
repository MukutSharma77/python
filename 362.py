'''Valid Zip Code
Zip codes consist of 5 consecutive digits. Given a string, write a function to determine whether the input is a valid zip code. A valid zip code is as follows:
Must only contain numbers (no non-digits allowed).
Must not contain any spaces.
Must not be greater than 5 digits in length.
Examples
is_valid("59001") ➞ True
is_valid("853a7") ➞ False'''


num="59001"
if num.isdigit():
    print(True)
else:
    print(False)
