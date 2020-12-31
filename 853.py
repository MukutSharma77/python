'''Rearrange the Number
Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits are rearranged.
Examples
rearranged_difference(972882) ➞ 760833
# 988722 - 227889 = 760833
rearranged_difference(3320707) ➞ 7709823
# 7733200 - 23377 = 7709823
rearranged_difference(90010) ➞ 90981
# 91000 - 19 = 90981'''


def rearranged_difference(num):
    lst_=[i for i in str(num)]
    # print(lst_)
    max_=sorted(lst_,reverse=True)
    # print(max_)
    min_=sorted(lst_)
    # print(min_)
    print(int(''.join(max_))-int(''.join(min_)))
rearranged_difference(972882)
rearranged_difference(3320707)
rearranged_difference(90010)
