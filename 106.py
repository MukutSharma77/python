#Python Program to Read a List of Words and Return the Length of the Longest One

list_=['mukut' ,'Sharma','aaaaaaaaaaaaaaaaaa' , 'Ghanshyam']

max_=list_[0]

for i in list_:
    if len(i) > len(max_):
        max_=i

print("The maximum length  :  ",max_)