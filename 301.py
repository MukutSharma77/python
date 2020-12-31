'''Letter Occurrences Per Word
Create a function that takes in a sentence and a character to find. Return a dictionary of each word in the sentence, with the number of the specified character as the value.
Examples
find_occurrences("Hello World", "o") ➞ {
  "hello" : 1,
  "world" : 1
}
find_occurrences("Create a nice JUICY function", "c") ➞  {
  "create" : 1,
  "a" : 0,
  "nice" : 1,
  "juicy" : 1,
  "function" : 1
}'''

def function(string):
    dict_={}
    search=input("Find :   ")
    for i in string:
        dict_[i]=i.count(search)

    print(dict_)



string='Create a nice JUICY function'.lower().split(' ')
function(string)