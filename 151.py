#Print number with commas as thousands separators in Python

def comma(num):
    return "{:,}".format(num)


number=int(input("Enter Number :   "))
result=comma(number)
print(result)