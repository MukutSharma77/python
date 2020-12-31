'''
Write a Python program to find the list of words that are longer than n from a given list of words
long_word(4)
long_word(6)
Output :
['Name', 'Mukut', 'Love', 'Python']
['Python']


'''
def long_word(n):
    lst=['My' , 'Name' , 'is' , 'Mukut' , 'And' , 'I' , 'Am' , 'a' ,'Boy' , 'Love' , 'Python']
    lst_new=[i for i in lst if len(i)>=n]
    print(lst_new)

long_word(4)
long_word(6)