'''Longest Sequence of Consecutive Zeroes
Write a function that returns the longest sequence of consecutive zeroes in a binary string.
Examples
longest_zero("01100001011000") ➞ "0000"
longest_zero("100100100") ➞ "00"
longest_zero("11111") '''

def longest_zero(string):
    string=string.split('1')
    # print(string)
    stru=[]
    for i in string:
        if i:
            stru.append(i)
    stru.sort()

    if stru:
        print(stru[-1])
    else:
        print("'''")
longest_zero("01100001011000")
longest_zero("100100100")
longest_zero("11111")