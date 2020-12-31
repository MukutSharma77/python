'''Write a Python program to check common elements between two given list are in same order or not.
color1=['red', 'green', 'black', 'orange']
color2=['red', 'pink', 'green', 'white', 'black']
color3=['white', 'orange', 'pink', 'black']
test( color1 , color2)
test( color1 , color3)
test( color2 , color3)
Output:
True
False
False'''

def test(chck1,chck2):
    count=0
    if len(chck1) >len(chck2):
        for i in range(len(chck2)):
            if chck2[i]==chck1[i]:
                count+=1
    else:
        for i in range(len(chck1)):
            if chck2[i]==chck1[i]:
                count+=1

    print(count>0)



color1=['red', 'green', 'black', 'orange']
color2=['red', 'pink', 'green', 'white', 'black']
color3=['white', 'orange', 'pink', 'black']
test( color1 , color2)
test( color1 , color3)
test( color2 , color3)
