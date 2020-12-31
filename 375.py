'''The 3 Programmers Problem
You hired three programmers and you (hopefully) pay them. Create a function that takes three numbers (the hourly wages of each programmer) and returns the difference between the highest-paid programmer and the lowest-paid.
Examples
programmers(147, 33, 526) ➞ 493
programmers(33, 72, 74) ➞ 41'''

list_=[147,33,526]
print(max(list_)-min(list_))