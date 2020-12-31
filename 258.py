'''Create a function that takes three arguments (first dictionary, second dictionary, key) in order to:
Return the boolean True if both dictionaries have the same values for the same keys.
If the dictionaries don't match, return the string "Not the same", or the string "One's empty" if only one of the dictionaries contains the given key.
Examples
dict_first = { "sky": "temple", "horde": "orcs", "people": 12, "story": "fine", "sun": "bright" }
dict_second = { "people": 12, "sun": "star", "book": "bad" }'''


def function(dict1 , dict2):
    search=input("Search :   ")
    if dict1[search]==dict2[search]:
        print(True)
    else:
        print("Not the same")



dict1={"people": 12, "sun": "star", "book": "bad"}
dict2={"people": 12, "sun": "star", "book": "bad"}

if dict1 and dict2:
    function(dict1,dict2)
else:
    print("One dict is empty")
