'''Zip It, If You Can?
Given a list of women and a list of men, either:
Return "sizes don't match" if the two lists have different sizes.
If the sizes match, return a list of pairs, with the first woman paired with the first man, second woman paired with the second man, etc.
Examples
zip_it(["Elise", "Mary"], ["John", "Rick"])
 ➞ [("Elise", "John"), ("Mary", "Rick")]
zip_it(["Ana", "Amy", "Lisa"], ["Bob", "Josh"])
 ➞ "sizes don"t match"'''

def zip_it(list1,list2):
    if len(list1)==len(list2):
        x=[]
        for i in range(0,len(list1)):
           x.append([list1[i],list2[i]])
        print(tuple(x))
    else:print("Size dont't match")

list1=["Elise", "Mary"]
list2=["John", "Rick"]

zip_it(list1,list2)