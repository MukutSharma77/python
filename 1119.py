'''Secret Function 4.0
Create a function based on the input and output. Look at the examples, there is a pattern.
Examples
secret("p.one.two.three") ➞ "<p class='one two three'></p>"
secret("p.one") ➞ "<p class='one'></p>"
secret("p.four.five") ➞ "<p class='four five'></p>"'''

def secret(string):
    string=string.split('.')
    store=''
    for i in string:
        store+=i+' '

    print(f"<p class='{store}'></p>")


secret("p.one.two.three")
secret("p.one")
secret("p.four.five")