'''Add Two String Numbers
Write a function that adds two numbers. The catch, however, is that the numbers will be strings.
add_str_nums("4", "5") ➞ "9"
add_str_nums("abcdefg", "3") ➞ "-1"
add_str_nums("1", "") ➞ "1"
add_str_nums("1874682736267235927359283579235789257", "32652983572985729") ➞ "1874682736267235927391936562808774986"'''

def add_str_nums(str1 , str2):
    eq=str1+'+'+str2
    if str2.isalpha() or str1.isalpha():
        print(-1)
    elif str1.isdigit() and str2=='' :
        print(str1)

    elif str2.isdigit() and str1=='':
        print(str2)

    else:
        print(eval(eq))

add_str_nums("4", "5")
add_str_nums("abcdefg", "3")
add_str_nums("1", "")
add_str_nums("1874682736267235927359283579235789257", "32652983572985729")