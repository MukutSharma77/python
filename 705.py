'''te a function that returns a list of the given string but offset by spaces. Here are some more precise instructions:
Keep adding spaces on the left until you have the same number of spaces as the word length.
Then keep removing spaces until you reach the original word.
Below are some helpful examples!
Examples
wiggle_string("hello") ➞ [
  "hello",
  " hello",
  "  hello",
  "   hello",
  "    hello",
  "     hello"
  "    hello",
  "   hello",
  "  hello",
  " hello",
  "hello"
]'''

string='hello'
lst=[]
for i in range(len(string)):
    lst.append((' ' * i) + string)

for i in range(len(string),-1,-1):
    lst.append((' ' * i) + string)


for i in lst:
    print(i+',')