'''Math Marking
Given a list of math equations (given as strings), return the percentage of correct answers as a string. Round to the nearest whole number.
Examples
mark_maths(["2+2=4", "3+2=5", "10-3=3", "5+5=10"]) ➞ "75%"
mark_maths(["1-2=-2"]), "0%"
mark_maths(["2+3=5", "4+4=9", "3-1=2"]) ➞ "67%"
Notes
You can expect only addition and subtraction.
Note how there aren't any spaces in any given equation.'''

def mark_maths(lst):
    count=0
    for i in lst:
        i=i.replace('=','==')
        if eval(i):
            count+=1

    print(str(round((count/len(lst))*100))+'%')


mark_maths(["2+2=4", "3+2=5", "10-3=3", "5+5=10"])
mark_maths(["1-2=-2"])
mark_maths(["2+3=5", "4+4=9", "3-1=2"])