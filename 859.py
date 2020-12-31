'''Count and Identify Data Types
Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. Finally return the total in a list.
List order is:
[int, str, bool, list, tuple, dictionary]
Examples
count_datatypes(1, 45, "Hi", False) ➞ [2, 1, 1, 0, 0, 0]
count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1) ➞ [3, 0, 0, 1, 1, 0]
count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23) ➞ [2, 2, 3, 1, 0, 2]
count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]) ➞ [2, 0, 1, 2, 2, 0]'''

def count_datatypes(*args):
    int_=0
    str_=0
    bool_=0
    list_=0
    tuple_=0
    dict_=0
    for i in args:
        if type(i)==int:
            int_+=1
        elif type(i) ==str:
            str_+=1
        elif type(i)==list:
            list_+=1
        elif type(i)==bool:
            bool_+=1
        elif type(i)==tuple:
            tuple_+=1
        elif type(i)==dict:
            dict_+=1

    lst=[int_,str_,bool_,list_,tuple_,dict_]
    print(lst)


count_datatypes(1, 45, "Hi", False)
count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1)
count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23)
count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6])