'''Calculate the Shortest Distance Between Two Points
Create a function that takes a string of four numbers. These numbers represent two separate points on a graph known as the x-axis (horizontal axis) and y-axis (vertical axis).
The order of coordinates in the string corresponds as follows:
"x1,y1,x2,y2"
Calculate the distance between x and y.
Examples
shortestDistance("1,1,2,1") ➞ 1
shortestDistance("1,1,3,1") ➞ 2
shortestDistance("-5,1,3,1") ➞ 8
shortestDistance("-5,2,3,1") ➞ 8.06
Notes
sqrt((x1-x2)**2 + (y1 - y2) ** 2)'''

def shortestDistance(string):
    import  math
    string=string.split(',')
    x1=int(string[0])
    x2=int(string[1])
    x3=int(string[2])
    x4=int(string[3])
    print(round(math.sqrt((x1-x3)**2 + (x2 - x4) ** 2),2))


shortestDistance("1,1,2,1")
shortestDistance("1,1,3,1")
shortestDistance("-5,1,3,1")
shortestDistance("-5,2,3,1")
