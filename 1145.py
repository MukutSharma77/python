'''Count Missing Numbers
Create a function that takes a list of "mostly" numbers, counts the amount of missing numbers and returns their sum. Watch out for strings!
Examples
count_missing_nums(["1", "3", "5", "7", "9"]) ➞ 4
count_missing_nums(["7", "3", "1", "9", "5"]) ➞ 4
count_missing_nums(["1", "5", "B", "9", "z"]) ➞ 6
Use:
max(s) - min(s) - len(s) + 1'''

def count_missing_nums(lst):
    lst_dgt=[int(i) for i in lst if i.isdigit()]
    print(max(lst_dgt) - min(lst_dgt) - len(lst_dgt) + 1)


count_missing_nums(["1", "3", "5", "7", "9"])
count_missing_nums(["7", "3", "1", "9", "5"])
count_missing_nums(["1", "5", "B", "9", "z"])