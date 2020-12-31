'''Track the Robot (Part 1)
A robot has been given a list of movement instructions. Each instruction is either left, right, up or down, followed by a distance to move. The robot starts at [0, 0]. You want to calculate where the robot will end up and return its final position as a list.
To illustrate, if the robot is given the following instructions:
["right 10", "up 50", "left 30", "down 10"]
It will end up 20 left and 40 up from where it started, so we return [-20, 40].
Examples
track_robot(["right 10", "up 50", "left 30", "down 10"]) ➞ [-20, 40]
track_robot([]) ➞ [0, 0]
// If there are no instructions, the robot doesn't move.
track_robot(["right 100", "right 100", "up 500", "up 10000"]) ➞ [200, 10500]'''


def track_robot(lst):
    dict_={
        'right' : 0,
        'left'  : 0,
        'up'    : 0,
        'down'  : 0
    }

    for i in lst:
        i=i.split(' ')
        dict_[i[0]]+=int(i[-1])

    lst_output=[dict_['right'] - dict_['left'] , dict_['up'] - dict_['down']]
    print(lst_output)


track_robot(["right 10", "up 50", "left 30", "down 10"])
track_robot([])
track_robot(["right 100", "right 100", "up 500", "up 10000"])