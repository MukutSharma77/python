'''Video Length in Seconds
You are given the length of a video in minutes. The format is mm:ss (e.g.: "02:54"). Create a function that takes the video length and return it in seconds.
Examples
minutes_to_seconds("01:00") ➞ 60
minutes_to_seconds("13:56") ➞ 836
minutes_to_seconds("10:60") ➞ False'''

min='10:60'.split(':')

if int(min[1])>59:
    print(False)
else:
    print((int(min[0]) * 60) + int(min[1]) )