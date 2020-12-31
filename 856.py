'''First Before Second Letter
You are given three inputs: a string, one letter, and a second letter.
Write a function that returns True if every instance of the first letter occurs before every instance of the second letter.
Examples
first_before_second("a rabbit jumps joyfully", "a", "j") ➞ True
# Every instance of "a" occurs before every instance of "j".
first_before_second("knaves knew about waterfalls", "k", "w") ➞  True
first_before_second("happy birthday", "a", "y") ➞ False
# The "a" in "birthday" occurs after the "y" in "happy".
first_before_second("precarious kangaroos", "k", "a") ➞ False'''

def first_before_second(string,ch1,ch2):
    print(string.rindex(ch1) < string.index(ch2))



first_before_second("a rabbit jumps joyfully", "a", "j")
first_before_second("knaves knew about waterfalls", "k", "w")
first_before_second("happy birthday", "a", "y")
first_before_second("precarious kangaroos", "k", "a")