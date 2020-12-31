'''Write a Python program to check if a substring presents in a given list of string values. Go to the editor
Original list:
check(['red', 'black', 'white', 'green', 'orange'],'ack')
check(['red', 'black', 'white', 'green', 'orange'],'abc')
Output:
True
False'''

def check(lst,str_):
    count=0
    for i in lst:
        if str_ in i:
            count+=1

    print(count==1)
check(['red', 'black', 'white', 'green', 'orange'],'ack')
check(['red', 'black', 'white', 'green', 'orange'],'abc')
