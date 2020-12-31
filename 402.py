'''Create a function that returns the index of the first vowel in a string.'''

string='My name is Mukut'.lower()

for i in  string:
    if i=='a' or i =='e' or i=='i' or i=='o' or i=='u' :
        print(string.index(i))
        break