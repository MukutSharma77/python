'''Create a function that repeats each character in a string n times.
Examples
repeat("mice", 5) ➞ "mmmmmiiiiiccccceeeee"
repeat("hello", 3) ➞ "hhheeellllllooo"'''

string='mice'
time=1
string2=''
for i in string:
    string2+=(i*time)

print(string2)