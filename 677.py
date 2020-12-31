'''Construct and Deconstruct
Given a string, create a function that outputs a list, building and deconstructing the string letter by letter. See the examples below for some helpful guidance.
Examples
construct_deconstruct("Hello") ➞ [
  "H",
  "He",
  "Hel",
  "Hell",
  "Hello",
  "Hell",
  "Hel",
  "He",
  "H"
]
construct_deconstruct("edabit") ➞ [
  "e",
  "ed",
  "eda",
  "edab",
  "edabi",
  "edabit",
  "edabi",
  "edab",
  "eda",
  "ed",
  "e"
]'''


string='edabit'

for i in range(1,len(string)):
    for j in range(0,i):
        print(string[j],end="")
    print()


for i in range(len(string),0,-1):
    for j in range(0,i):
        print(string[j],end="")
    print()