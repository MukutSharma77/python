'''Encoded String Parse
Create a function which takes in an encoded string and returns a dictionary according to the following example:
Examples
parse_code("John000Doe000123") ➞ {
  "first_name": "John",
  "last_name": "Doe",
  "id": "123"
}
parse_code("michael0smith004331") ➞ {
  "first_name": "michael",
  "last_name": "smith",
  "id": "4331"
}
parse_code("Thomas00LEE0000043") ➞ {
  "first_name": "Thomas",
  "last_name": "LEE",
  "id": "43"
}'''


def parse_code(string):
    string=string.split('0')
    lst_=[i for i in string if i.isalpha() or i.isdigit()]
    dic_={
        'first_name' : lst_[0],
        'last_name'  : lst_[1],
        'id' : lst_[2]
    }
    print(dic_)


parse_code("John000Doe000123")
parse_code("michael0smith004331")
parse_code("Thomas00LEE0000043")