'''Let's Meet!
From point A, an object is moving towards point B at constant velocity va (in km/hr). From point B, another object is moving towards point A at constant velocity vb (in km/hr). Knowing this and the distance between point A and B (in km), write a function that returns how much time passes until both objects meet.
Format the output like this:
"2h 23min 34s"
Examples
lets_meet(100, 10, 30) ➞ "2h 30min 0s"
lets_meet(280, 70, 80) ➞ "1h 52min 0s"
lets_meet(90, 75, 65) ➞ "0h 38min 34s"
Use:
int(3600*distance/(va+vb))'''


def lets_meet(distance , va , vb):
    time=3600*distance/(va+vb)
    hour=time//3600
    print(str(int(hour))+'h',end=" ")
    time=time - (hour * 3600)
    min=time // 60
    time = time - min*60
    print(str(int(min)) + 'min', end=" ")

    print(str(str(int(time))+'s'))

lets_meet(100, 10, 30)
lets_meet(280, 70, 80)
lets_meet(90, 75, 65)