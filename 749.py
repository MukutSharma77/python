'''Ones, Threes and Nines (Version #1)
Given an int, figure out how many ones, threes and nines you could fit into the number. You must create a class. You will make variables(self.ones, self.threes, self.nines) to do this.
Examples
n1 = ones_threes_nines(5)
n1.nines ➞ 0
n1.ones ➞ 5
n1.threes ➞ 1'''

class ones_threes_nines:
    def __init__(self,num):
        self.num=num

    def nines(self):
        print(self.num//9)

    def ones(self):
        print(self.num // 1)

    def three(self):
        print(self.num//3)

n1 = ones_threes_nines(5)
n1.nines()
n1.ones()
n1.three()