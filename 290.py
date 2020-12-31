'''Create a function that returns the list of numbers from a given range. But for multiples of three, return “Eda” instead of the number and for the multiples of five, return “Bit”. For numbers which are multiples of both three and five, return “EdaBit”.
Examples
eda_bit(0, 10) ➞ ["EdaBit", 1, 2, "Eda", 4, "Bit", "Eda", 7, 8, "Eda", "Bit" ]
eda_bit(14, 20) ➞ [14,  "EdaBit", 16, 17,  "Eda", 19, "Bit" ]
'''


def function():
    num_to=int(input("Number to :   "))
    num_from=int(input("Number from :   "))
    list_=[]
    for i in range(num_to,num_from+1):
        if i % 3 == 0 and i % 5 ==0:
            list_.append('Edabit')

        elif i % 3==0:
            list_.append('Eda')


        elif i % 5 == 0:
            list_.append('Bit')

        else:
            list_.append(i)

    print(list_)
function()