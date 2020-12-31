'''Sum of Decimals
Examples
float_sum(0.3, 0.7) ➞ 1
float_sum(0.35, 0.75) ➞ 1.1
float_sum(1.234, 5.6789) ➞ 6.9129'''

def float_sum(num1,num2):
    tot=num2+num1
    tot_=str(tot).split('.')
    if ''.join(tot_[-2:])=='10':
        print(int(tot))
    else:
        print(tot)


float_sum(1.234, 5.6789)