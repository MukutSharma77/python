'''Algebra Sequence — Boxes
Create a function that takes a number (step) as an argument and returns the amount of boxes in that step of the sequence.
Box Sequence Image
Step 0: Start with 0
Step 1: Add 3
Step 2: Subtract 1
Repeat Step 1 & 2 ...
Examples
box_seq(0) ➞ 0
box_seq(1) ➞ 3
box_seq(2) ➞ 2'''

def box_seq(n):
    output=0
    if n >= 0:
        for i in range(1,n+1):
            if i % 2==1:
                output+=3

            else:
                output-=1
    print(output)




box_seq(0)
box_seq(1)
box_seq(2)