'''check whether person is eligible for voting or not using Ternary operator.
hint	: 	    [on_true] if [expression] else [on_false]'''

age=int(input("Enter your age :   "))
msg="yes you can vote " if age >= 18 else 'Cant vote'
print(msg)