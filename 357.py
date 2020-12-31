'''Create a function that takes a number and "m" (for male) or "f" (for female), and returns the name of an ancestor (m/f) or descendant (m/f).
If the number is negative, return the related ancestor.
If positive, return the related descendant.
You are generation 0. In the case of 0 (male or female), return "me!".
Examples
generation(2, "f") ➞ "granddaughter"
generation(-3, "m") ➞ "great grandfather"
generation(1, "f") ➞ "daughter"
Generation	Male	Female
-3	great grandfather	great grandmother
-2	grandfather	grandmother
-1	father	mother
0	me!	me!
1	son	daughter
2	grandson	granddaughter
3	great grandson	great granddaughter

'''

def generation(no,gender):
    dict_={
        -3 : {'f' : 'Great Grandmother','m':'Great Grandfather'},
        -2 : {'f' : 'Grandmother','m':'Grandfather'},
        -1 : {'f' : 'Mother','m':'Father'},
         0 : {'f' : 'ME','m':'ME'},
         1 : {'f' : 'Daughter','m':'Son'},
         2 : {'f' : 'Mother','m':'Father'},
         3 : {'f' : 'Great Grandson','m':'Great Granddaughter'}
    }
    if no in dict_:
        print(dict_[no][gender])
    else:
        print("Not founf")
generation(2, "f")
generation(-3, "m")
generation(1, "f")