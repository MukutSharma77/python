'''Given what is supposed to be typed and what is actually typed, write a function that returns the broken key(s). The function looks like:
find_broken_keys(correct phrase, what you actually typed)
Examples
find_broken_keys("happy birthday", "hawwy birthday") ➞ ["p"]
find_broken_keys("starry night", "starrq light") ➞ ["y", "n"]
find_broken_keys("beethoven", "affthoif5") ➞ ["b", "e", "v", "n"]
'''

def function(correct_phase,wrong_phase):
    list_=[]

    for i in correct_phase:
        if i not in wrong_phase:
            list_.append(i)

    print(list(set(list_)))

correct_phase='starry night'
wrong_phase='starrq light'
function(correct_phase,wrong_phase)