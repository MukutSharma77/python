'''Tower of Hanoi
There are three towers. The objective of the game is to move all the disks over to tower #3, but you can't place a larger disk onto a smaller disk. To play the game or learn more about the Tower of Hanoi, check the Resources tab.
Tower of Hanoi
Create a function that takes a number discs as an argument and returns the minimum amount of steps needed to complete the game.
Examples
tower_hanoi(3) ➞ 7
tower_hanoi(5) ➞ 31
tower_hanoi(0) ➞ 0
n:2**n-1'''

tower_hanoi=lambda num:2**num-1

num=0
output=tower_hanoi(num)
print(output)

