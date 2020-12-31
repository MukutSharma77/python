'''Create a function that returns the data type of a given variable. These are the seven data types this challenge will be testing for:
List
Dictionary
String
Integer
Float
Boolean
Date
Examples
data_type([1, 2, 3, 4]) ➞ "list"
data_type({'key': "value"}) ➞ "dictionary"
data_type("This is an example string.") ➞ "string"
data_type(datetime.date(2018,1,1)) ➞ "date"'''

import  datetime
dict_={
    list : 'List',
    dict : 'Dictionary',
    str : 'string',
    int : 'Intiger',
    float : 'Float',
    bool : 'Boolean',
    datetime.date : 'datetime.date'
}

string='hey'
print(dict_.get(type(string)))