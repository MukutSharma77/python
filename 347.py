'''Create a function that takes two strings and returns True if the first string ends with the second string; otherwise return False.
Examples
check_ending("abc", "bc") ➞ True
check_ending("abc", "d") ➞ False
check_ending("samurai", "zi") ➞ False
check_ending("feminine", "nine") ➞ True
'''

def check_ending(string , ch):
    print(string[len(string)-len(ch) : ]==ch)

check_ending("abc", "bc")
check_ending("abc", "d")
check_ending("samurai", "zi")
check_ending("feminine", "nine")
